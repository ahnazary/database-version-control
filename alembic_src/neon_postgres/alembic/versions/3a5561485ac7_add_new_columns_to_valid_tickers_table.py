"""add new columns to valid_tickers table

Revision ID: 3a5561485ac7
Revises: 5683f058b7e0
Create Date: 2023-11-01 21:34:20.706895

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a5561485ac7"
down_revision: Union[str, None] = "5683f058b7e0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add 8 new columns to valid_tickers table with names being with defualt value of True
    #   - balance_sheet_annual_available
    #   - cashflow_annual_available
    #   - income_stmt_annual_available
    #   - financials_annual_available
    #   - balance_sheet_quarterly_available
    #   - cashflow_quarterly_available
    #   - income_stmt_quarterly_available
    #   - financials_quarterly_available
    op.add_column(
        "valid_tickers",
        sa.Column(
            "balance_sheet_annual_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "cashflow_annual_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "income_stmt_annual_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "financials_annual_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "balance_sheet_quarterly_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "cashflow_quarterly_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "income_stmt_quarterly_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )
    op.add_column(
        "valid_tickers",
        sa.Column(
            "financials_quarterly_available",
            sa.Boolean(),
            nullable=True,
            server_default="True",
        ),
        schema="stocks",
    )


def downgrade() -> None:
    # drop columns if they exist
    op.drop_column("valid_tickers", "balance_sheet_annual_available", schema="stocks")
    op.drop_column("valid_tickers", "cashflow_annual_available", schema="stocks")
    op.drop_column("valid_tickers", "income_stmt_annual_available", schema="stocks")
    op.drop_column("valid_tickers", "financials_annual_available", schema="stocks")
    op.drop_column(
        "valid_tickers", "balance_sheet_quarterly_available", schema="stocks"
    )
    op.drop_column("valid_tickers", "cashflow_quarterly_available", schema="stocks")
    op.drop_column("valid_tickers", "income_stmt_quarterly_available", schema="stocks")
    op.drop_column("valid_tickers", "financials_quarterly_available", schema="stocks")
