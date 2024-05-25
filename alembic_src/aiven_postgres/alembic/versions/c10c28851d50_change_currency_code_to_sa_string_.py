"""change currency_code to sa.String(length=100)

Revision ID: c10c28851d50
Revises: dacd323cc69b
Create Date: 2024-01-29 00:55:11.277115

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c10c28851d50"
down_revision: Union[str, None] = "dacd323cc69b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # update balance_Sheet currency_code to sa.String(length=100)
    op.alter_column(
        "balance_sheet",
        "currency_code",
        existing_type=sa.String(length=3),
        type_=sa.String(length=100),
        existing_nullable=True,
        schema="stocks",
    )
    op.alter_column(
        "cashflow",
        "currency_code",
        existing_type=sa.String(length=3),
        type_=sa.String(length=100),
        existing_nullable=True,
        schema="stocks",
    )
    op.alter_column(
        "income_stmt",
        "currency_code",
        existing_type=sa.String(length=3),
        type_=sa.String(length=100),
        existing_nullable=True,
        schema="stocks",
    )
    op.alter_column(
        "financials",
        "currency_code",
        existing_type=sa.String(length=3),
        type_=sa.String(length=100),
        existing_nullable=True,
        schema="stocks",
    )


def downgrade() -> None:
    pass
