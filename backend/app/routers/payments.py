import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_current_user_id
from app.models.payment import PaymentRequest
from app.models.course import Course, CourseEnrollment
from app.models.user import User
from app.schemas.payments import PaymentCreateRequest, PaymentResponse, PaymentReviewRequest
from app.routers.admin import get_admin_user
from app.services import course_service

router = APIRouter(tags=["payments"])


# ── User endpoints ────────────────────────────────────────

@router.post("/api/payments/request")
async def create_payment_request(
    body: PaymentCreateRequest,
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    course_id = uuid.UUID(body.course_id)

    # Check course exists and has a price
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.price <= 0:
        raise HTTPException(status_code=400, detail="This course is free, no payment needed")

    # Check user not already enrolled
    enrollment = await db.execute(
        select(CourseEnrollment).where(
            CourseEnrollment.user_id == user_id,
            CourseEnrollment.course_id == course_id,
        )
    )
    if enrollment.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Already enrolled in this course")

    # Check no pending payment for the same course
    pending = await db.execute(
        select(PaymentRequest).where(
            PaymentRequest.user_id == user_id,
            PaymentRequest.course_id == course_id,
            PaymentRequest.status == "pending",
        )
    )
    if pending.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="You already have a pending payment for this course")

    payment = PaymentRequest(
        user_id=user_id,
        course_id=course_id,
        amount=course.price,
        currency=course.currency,
        screenshot_url=body.screenshot_url,
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)

    return {
        "id": str(payment.id),
        "course_id": str(payment.course_id),
        "amount": payment.amount,
        "currency": payment.currency,
        "status": payment.status,
        "created_at": payment.created_at.isoformat() if payment.created_at else None,
    }


@router.get("/api/payments/my")
async def list_my_payments(
    user_id: uuid.UUID = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(PaymentRequest, Course.title)
        .join(Course, PaymentRequest.course_id == Course.id)
        .where(PaymentRequest.user_id == user_id)
        .order_by(PaymentRequest.created_at.desc())
    )
    rows = result.all()

    return [
        {
            "id": str(p.id),
            "course_id": str(p.course_id),
            "course_title": title,
            "amount": p.amount,
            "currency": p.currency,
            "screenshot_url": p.screenshot_url,
            "status": p.status,
            "admin_note": p.admin_note,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "reviewed_at": p.reviewed_at.isoformat() if p.reviewed_at else None,
        }
        for p, title in rows
    ]


# ── Admin endpoints ───────────────────────────────────────

@router.get("/api/admin/payments")
async def list_pending_payments(
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(PaymentRequest, Course.title, User.name, User.email)
        .join(Course, PaymentRequest.course_id == Course.id)
        .join(User, PaymentRequest.user_id == User.id)
        .order_by(
            # pending first, then by date
            PaymentRequest.status.desc(),
            PaymentRequest.created_at.desc(),
        )
    )
    rows = result.all()

    return [
        PaymentResponse(
            id=str(p.id),
            course_id=str(p.course_id),
            course_title=course_title,
            user_name=user_name or "",
            user_email=user_email or "",
            amount=p.amount,
            currency=p.currency,
            screenshot_url=p.screenshot_url,
            status=p.status,
            admin_note=p.admin_note,
            created_at=p.created_at,
            reviewed_at=p.reviewed_at,
        ).model_dump()
        for p, course_title, user_name, user_email in rows
    ]


@router.post("/api/admin/payments/{payment_id}/review")
async def review_payment(
    payment_id: uuid.UUID,
    body: PaymentReviewRequest,
    admin_id: uuid.UUID = Depends(get_admin_user),
    db: AsyncSession = Depends(get_db),
):
    if body.action not in ("approve", "reject"):
        raise HTTPException(status_code=400, detail="Action must be 'approve' or 'reject'")

    result = await db.execute(
        select(PaymentRequest).where(PaymentRequest.id == payment_id)
    )
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment request not found")
    if payment.status != "pending":
        raise HTTPException(status_code=409, detail="Payment already reviewed")

    now = datetime.now(timezone.utc)

    if body.action == "approve":
        payment.status = "approved"
        payment.reviewed_at = now
        payment.reviewed_by = admin_id
        payment.admin_note = body.note

        # Enroll the user in the course
        await course_service.enroll(db, payment.user_id, payment.course_id)

    elif body.action == "reject":
        payment.status = "rejected"
        payment.reviewed_at = now
        payment.reviewed_by = admin_id
        payment.admin_note = body.note

    await db.commit()
    await db.refresh(payment)

    return {
        "id": str(payment.id),
        "status": payment.status,
        "reviewed_at": payment.reviewed_at.isoformat() if payment.reviewed_at else None,
        "admin_note": payment.admin_note,
    }
