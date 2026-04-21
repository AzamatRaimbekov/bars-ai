from pydantic import BaseModel
from datetime import datetime


class PaymentCreateRequest(BaseModel):
    course_id: str
    screenshot_url: str  # base64 data URL from frontend


class PaymentResponse(BaseModel):
    id: str
    course_id: str
    course_title: str
    user_name: str
    user_email: str
    amount: int
    currency: str
    screenshot_url: str
    status: str
    admin_note: str | None
    created_at: datetime
    reviewed_at: datetime | None


class PaymentReviewRequest(BaseModel):
    action: str  # "approve" or "reject"
    note: str | None = None
