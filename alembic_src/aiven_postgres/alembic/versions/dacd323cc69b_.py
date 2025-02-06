"""Initiate new tables with json column

Revision ID: 6de3f850c165
Revises: 49217d5d1147
Create Date: 2025-02-06 23:42:31.740377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dacd323cc69b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "financials",
        sa.Column("ticker", sa.String(length=100), nullable=False),
        sa.Column("insert_date", sa.Date(), nullable=False),
        sa.Column("report_date", sa.Date(), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=True),
        sa.Column("frequency", sa.String(length=10), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("ticker", "insert_date", "report_date", "frequency"),
        schema="finance",
    )

    op.create_table(
        "income_stmt",
        sa.Column("ticker", sa.String(length=100), nullable=False),
        sa.Column("insert_date", sa.Date(), nullable=False),
        sa.Column("report_date", sa.Date(), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=True),
        sa.Column("frequency", sa.String(length=10), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("ticker", "insert_date", "report_date", "frequency"),
        schema="finance",
    )

    op.create_table(
        "balance_sheet",
        sa.Column("ticker", sa.String(length=100), nullable=False),
        sa.Column("insert_date", sa.Date(), nullable=False),
        sa.Column("report_date", sa.Date(), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=True),
        sa.Column("frequency", sa.String(length=10), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("ticker", "insert_date", "report_date", "frequency"),
        schema="finance",
    )

    op.create_table(
        "cashflow",
        sa.Column("ticker", sa.String(length=100), nullable=False),
        sa.Column("insert_date", sa.Date(), nullable=False),
        sa.Column("report_date", sa.Date(), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=True),
        sa.Column("frequency", sa.String(length=10), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("ticker", "insert_date", "report_date", "frequency"),
        schema="finance",
    )

    op.create_table(
        "valid_tickers",
        sa.Column("ticker", sa.String(length=100), nullable=False),
        sa.Column("currency_code", sa.String(length=10), nullable=True),
        sa.PrimaryKeyConstraint("ticker"),
        schema="finance",
    )


def downgrade() -> None:
    op.drop_table("valid_tickers", schema="finance")
    op.drop_table("cashflow", schema="finance")
    op.drop_table("balance_sheet", schema="finance")
    op.drop_table("income_stmt", schema="finance")
    op.drop_table("financials", schema="finance")
