"""add sprints and trophy_events tables, user role field

Revision ID: a3f7b8c9d012
Revises: d1ceba14222a
Create Date: 2026-04-14 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a3f7b8c9d012'
down_revision: Union[str, None] = 'd1ceba14222a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add role column to users
    op.add_column('users', sa.Column('role', sa.String(length=20), nullable=True))
    op.execute("UPDATE users SET role = 'user' WHERE role IS NULL")
    op.execute("UPDATE users SET role = 'admin' WHERE email = 'superadmin@pathmind.com'")
    op.alter_column('users', 'role', nullable=False, server_default='user')

    # Create sprints table
    op.create_table('sprints',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('start_date', sa.DateTime(timezone=True), nullable=False),
        sa.Column('end_date', sa.DateTime(timezone=True), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.Column('prizes', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('winners', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_by', sa.UUID(), nullable=True),
        sa.Column('closed_by', sa.UUID(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['created_by'], ['users.id']),
        sa.ForeignKeyConstraint(['closed_by'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Create trophy_events table
    op.create_table('trophy_events',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('sprint_id', sa.UUID(), nullable=True),
        sa.Column('action', sa.String(length=30), nullable=False),
        sa.Column('trophies', sa.Integer(), nullable=False),
        sa.Column('metadata_json', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('trophy_events')
    op.drop_table('sprints')
    op.drop_column('users', 'role')
