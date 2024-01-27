"""Change string column types to get more cahrs

Revision ID: 222648ce9bb9
Revises: 5265a3bc1429
Create Date: 2023-11-13 22:56:10.400008

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "222648ce9bb9"
down_revision: Union[str, None] = "5265a3bc1429"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # change following string columns to varchar with no limit
    # "ticker"
    # "currency_code"
    # on tables balance_sheet, cashflow, income_stmt, financials, valid_tickers

    op.alter_column(
        "valid_tickers",
        "ticker",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "valid_tickers",
        "currency_code",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "balance_sheet",
        "ticker",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "balance_sheet",
        "currency_code",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "cashflow",
        "ticker",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "cashflow",
        "currency_code",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "income_stmt",
        "ticker",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "income_stmt",
        "currency_code",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "financials",
        "ticker",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )
    op.alter_column(
        "financials",
        "currency_code",
        existing_type=sa.VARCHAR(length=10),
        type_=sa.String(),
        schema="stocks",
    )


def downgrade() -> None:
    pass
