"""Add columns to balance_sheet table

Revision ID: f5c7e11c725f
Revises: 7632e55ed646
Create Date: 2023-11-20 22:43:23.146155

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f5c7e11c725f"
down_revision: Union[str, None] = "7632e55ed646"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add folowing columns to balance_sheet table:
    # capital_lease_obligations
    # fixed_assets_revaluation_reserve
    # non_current_deferred_revenue
    # long_term_capital_lease_obligation
    # current_capital_lease_obligation
    # other_payable
    # total_tax_payable
    # investmentin_financial_assets
    # long_term_equity_investment
    # investmentsin_associatesat_cost
    # other_properties
    # hedging_assets_current
    # other_receivables
    # cash_financial

    op.add_column(
        "balance_sheet",
        sa.Column("capital_lease_obligations", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("fixed_assets_revaluation_reserve", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("non_current_deferred_revenue", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("long_term_capital_lease_obligation", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("current_capital_lease_obligation", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("other_payable", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("total_tax_payable", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("investmentin_financial_assets", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("long_term_equity_investment", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("investmentsin_associatesat_cost", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("other_properties", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("hedging_assets_current", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("other_receivables", sa.Numeric(), nullable=True),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("cash_financial", sa.Numeric(), nullable=True),
        schema="stocks",
    )


def downgrade() -> None:
    # remove folowing columns from balance_sheet table:
    # capital_lease_obligations
    # fixed_assets_revaluation_reserve
    # non_current_deferred_revenue
    # long_term_capital_lease_obligation
    # current_capital_lease_obligation
    # other_payable
    # total_tax_payable
    # investmentin_financial_assets
    # long_term_equity_investment
    # investmentsin_associatesat_cost
    # other_properties
    # hedging_assets_current
    # other_receivables
    # cash_financial

    op.drop_column("balance_sheet", "capital_lease_obligations", schema="stocks")
    op.drop_column("balance_sheet", "fixed_assets_revaluation_reserve", schema="stocks")
    op.drop_column("balance_sheet", "non_current_deferred_revenue", schema="stocks")
    op.drop_column(
        "balance_sheet", "long_term_capital_lease_obligation", schema="stocks"
    )
    op.drop_column("balance_sheet", "current_capital_lease_obligation", schema="stocks")
    op.drop_column("balance_sheet", "other_payable", schema="stocks")
    op.drop_column("balance_sheet", "total_tax_payable", schema="stocks")
    op.drop_column("balance_sheet", "investmentin_financial_assets", schema="stocks")
    op.drop_column("balance_sheet", "long_term_equity_investment", schema="stocks")
    op.drop_column("balance_sheet", "investmentsin_associatesat_cost", schema="stocks")
    op.drop_column("balance_sheet", "other_properties", schema="stocks")
    op.drop_column("balance_sheet", "hedging_assets_current", schema="stocks")
    op.drop_column("balance_sheet", "other_receivables", schema="stocks")
    op.drop_column("balance_sheet", "cash_financial", schema="stocks")
