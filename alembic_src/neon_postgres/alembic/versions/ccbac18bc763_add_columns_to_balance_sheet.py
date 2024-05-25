"""Add columns to balance sheet

Revision ID: ccbac18bc763
Revises: f5c7e11c725f
Create Date: 2024-01-04 23:46:48.531280

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ccbac18bc763"
down_revision: Union[str, None] = "f5c7e11c725f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add following columns:
    # preferred_shares_number
    # preferred_stock_equity
    # dividends_payable
    # available_for_sale_securities
    # cash_equivalents

    op.add_column(
        "balance_sheet",
        sa.Column("preferred_shares_number", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("preferred_stock_equity", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("dividends_payable", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("available_for_sale_securities", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("cash_equivalents", sa.Float(), nullable=True),
        schema="stocks",
    )


def downgrade() -> None:
    op.drop_column("balance_sheet", "preferred_shares_number", schema="stocks")
    op.drop_column("balance_sheet", "preferred_stock_equity", schema="stocks")
    op.drop_column("balance_sheet", "dividends_payable", schema="stocks")
    op.drop_column("balance_sheet", "available_for_sale_securities", schema="stocks")
    op.drop_column("balance_sheet", "cash_equivalents", schema="stocks")
