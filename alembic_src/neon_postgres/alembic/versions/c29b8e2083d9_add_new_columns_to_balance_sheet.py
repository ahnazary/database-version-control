"""Add new columns to balance sheet

Revision ID: c29b8e2083d9
Revises: ccbac18bc763
Create Date: 2024-01-21 16:57:52.418027

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c29b8e2083d9"
down_revision: Union[str, None] = "ccbac18bc763"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add following columns to balance_sheet table
    # "treasury_shares_number"
    # "treasury_stock"
    # "non_current_deferred_taxes_liabilities"
    # "other_current_liabilities"
    # "investment_properties"
    # "current_deferred_assets"
    # "prepaid_assets"
    # "taxes_receivable"
    # "allowance_for_doubtful_accounts_receivable"
    # "gross_accounts_receivable"

    op.add_column(
        "balance_sheet",
        sa.Column("treasury_shares_number", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("treasury_stock", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("non_current_deferred_taxes_liabilities", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("other_current_liabilities", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("investment_properties", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("current_deferred_assets", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("prepaid_assets", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("taxes_receivable", sa.Float(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "allowance_for_doubtful_accounts_receivable", sa.Float(), nullable=True
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("gross_accounts_receivable", sa.Float(), nullable=True),
        schema="stocks",
    )


def downgrade() -> None:
    # drop following columns from balance_sheet table
    op.drop_column("balance_sheet", "treasury_shares_number", schema="stocks")
    op.drop_column("balance_sheet", "treasury_stock", schema="stocks")
    op.drop_column(
        "balance_sheet", "non_current_deferred_taxes_liabilities", schema="stocks"
    )
    op.drop_column("balance_sheet", "other_current_liabilities", schema="stocks")
    op.drop_column("balance_sheet", "investment_properties", schema="stocks")
    op.drop_column("balance_sheet", "current_deferred_assets", schema="stocks")
    op.drop_column("balance_sheet", "prepaid_assets", schema="stocks")
    op.drop_column("balance_sheet", "taxes_receivable", schema="stocks")
    op.drop_column(
        "balance_sheet", "allowance_for_doubtful_accounts_receivable", schema="stocks"
    )
    op.drop_column("balance_sheet", "gross_accounts_receivable", schema="stocks")
