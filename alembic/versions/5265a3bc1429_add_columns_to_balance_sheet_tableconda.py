"""Add columns to balance sheet tableconda

Revision ID: 5265a3bc1429
Revises: d80b41d91c36
Create Date: 2023-11-07 23:02:44.433895

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5265a3bc1429"
down_revision: Union[str, None] = "d80b41d91c36"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add following columns to balance_sheet table
    # ordinary_shares_number
    # share_issued
    # net_debt
    # total_debt
    # tangible_book_value
    # invested_capital
    # working_capital
    # net_tangible_assets
    # common_stock_equity
    # total_capitalization
    # total_equity_gross_minority_interest
    # stockholders_equity
    # gains_losses_not_affecting_retained_earnings
    # other_equity_adjustments
    # retained_earnings
    # additional_paid_in_capital
    # capital_stock
    # common_stock
    # preferred_stock
    # total_liabilities_net_minority_interest
    # total_non_current_liabilities_net_minority_interest
    # other_non_current_liabilities
    # employee_benefits
    # non_current_pension_and_other_postretirement_benefit_plans
    # long_term_debt_and_capital_lease_obligation
    # long_term_debt
    # current_liabilities
    # current_deferred_liabilities
    # current_deferred_revenue
    # current_debt_and_capital_lease_obligation
    # current_debt
    # commercial_paper
    # pensionand_other_post_retirement_benefit_plans_current
    # payables_and_accrued_expenses
    # current_accrued_expenses
    # payables
    # accounts_payable
    # total_assets
    # total_non_current_assets
    # other_non_current_assets
    # investments_and_advances
    # goodwill_and_other_intangible_assets
    # other_intangible_assets
    # goodwill
    # net_ppe
    # accumulated_depreciation
    # gross_ppe
    # machinery_furniture_equipment
    # buildings_and_improvements
    # land_and_improvements
    # properties
    # current_assets
    # other_current_assets
    # inventory
    # finished_goods
    # raw_materials
    # receivables
    # accounts_receivable
    # cash_cash_equivalents_and_short_term_investments
    # other_short_term_investments
    # cash_and_cash_equivalents

    op.add_column(
        "balance_sheet",
        sa.Column(
            "ordinary_shares_number",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "share_issued",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "net_debt",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_debt",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "tangible_book_value",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "invested_capital",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "working_capital",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "net_tangible_assets",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "common_stock_equity",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_capitalization",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_equity_gross_minority_interest",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "stockholders_equity",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "gains_losses_not_affecting_retained_earnings",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_equity_adjustments", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "retained_earnings", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "additional_paid_in_capital",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("capital_stock", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("common_stock", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("preferred_stock", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_liabilities_net_minority_interest",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_non_current_liabilities_net_minority_interest",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_non_current_liabilities",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "employee_benefits", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "non_current_pension_and_other_postretirement_benefit_plans",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "long_term_debt_and_capital_lease_obligation",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("long_term_debt", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "current_liabilities", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "current_deferred_liabilities",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "current_deferred_revenue", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "current_debt_and_capital_lease_obligation",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("current_debt", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("commercial_paper", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "pensionand_other_post_retirement_benefit_plans_current",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "payables_and_accrued_expenses",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "current_accrued_expenses", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("payables", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("accounts_payable", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("total_assets", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "total_non_current_assets", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_non_current_assets", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "investments_and_advances", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "goodwill_and_other_intangible_assets",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_intangible_assets", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("goodwill", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("net_ppe", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "accumulated_depreciation", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("gross_ppe", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "machinery_furniture_equipment",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "buildings_and_improvements",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "land_and_improvements", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("properties", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("current_assets", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_current_assets", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("inventory", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("finished_goods", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("raw_materials", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column("receivables", sa.Numeric(), nullable=True, server_default=None),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "accounts_receivable", sa.Numeric(), nullable=True, server_default=None
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "cash_cash_equivalents_and_short_term_investments",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "other_short_term_investments",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "balance_sheet",
        sa.Column(
            "cash_and_cash_equivalents",
            sa.Numeric(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )


def downgrade() -> None:
    # drop columns if they exist
    op.drop_column("balance_sheet", "ordinary_shares_number", schema="stocks")
    op.drop_column("balance_sheet", "share_issued", schema="stocks")
    op.drop_column("balance_sheet", "net_debt", schema="stocks")
    op.drop_column("balance_sheet", "total_debt", schema="stocks")
    op.drop_column("balance_sheet", "tangible_book_value", schema="stocks")
    op.drop_column("balance_sheet", "invested_capital", schema="stocks")
    op.drop_column("balance_sheet", "working_capital", schema="stocks")
    op.drop_column("balance_sheet", "net_tangible_assets", schema="stocks")
    op.drop_column("balance_sheet", "common_stock_equity", schema="stocks")
    op.drop_column("balance_sheet", "total_capitalization", schema="stocks")
    op.drop_column(
        "balance_sheet", "total_equity_gross_minority_interest", schema="stocks"
    )
    op.drop_column("balance_sheet", "stockholders_equity", schema="stocks")
    op.drop_column(
        "balance_sheet", "gains_losses_not_affecting_retained_earnings", schema="stocks"
    )
    op.drop_column("balance_sheet", "other_equity_adjustments", schema="stocks")
    op.drop_column("balance_sheet", "retained_earnings", schema="stocks")
    op.drop_column("balance_sheet", "additional_paid_in_capital", schema="stocks")
    op.drop_column("balance_sheet", "capital_stock", schema="stocks")
    op.drop_column("balance_sheet", "common_stock", schema="stocks")
    op.drop_column("balance_sheet", "preferred_stock", schema="stocks")
    op.drop_column(
        "balance_sheet", "total_liabilities_net_minority_interest", schema="stocks"
    )
    op.drop_column(
        "balance_sheet",
        "total_non_current_liabilities_net_minority_interest",
        schema="stocks",
    )
    op.drop_column("balance_sheet", "other_non_current_liabilities", schema="stocks")
    op.drop_column("balance_sheet", "employee_benefits", schema="stocks")
    op.drop_column(
        "balance_sheet",
        "non_current_pension_and_other_postretirement_benefit_plans",
        schema="stocks",
    )
    op.drop_column(
        "balance_sheet", "long_term_debt_and_capital_lease_obligation", schema="stocks"
    )
    op.drop_column("balance_sheet", "long_term_debt", schema="stocks")
    op.drop_column("balance_sheet", "current_liabilities", schema="stocks")
    op.drop_column("balance_sheet", "current_deferred_liabilities", schema="stocks")
    op.drop_column("balance_sheet", "current_deferred_revenue", schema="stocks")
    op.drop_column(
        "balance_sheet", "current_debt_and_capital_lease_obligation", schema="stocks"
    )
    op.drop_column("balance_sheet", "current_debt", schema="stocks")
    op.drop_column("balance_sheet", "commercial_paper", schema="stocks")
    op.drop_column(
        "balance_sheet",
        "pensionand_other_post_retirement_benefit_plans_current",
        schema="stocks",
    )
    op.drop_column("balance_sheet", "payables_and_accrued_expenses", schema="stocks")
    op.drop_column("balance_sheet", "current_accrued_expenses", schema="stocks")
    op.drop_column("balance_sheet", "payables", schema="stocks")
    op.drop_column("balance_sheet", "accounts_payable", schema="stocks")
    op.drop_column("balance_sheet", "total_assets", schema="stocks")
    op.drop_column("balance_sheet", "total_non_current_assets", schema="stocks")
    op.drop_column("balance_sheet", "other_non_current_assets", schema="stocks")
    op.drop_column("balance_sheet", "investments_and_advances", schema="stocks")
    op.drop_column(
        "balance_sheet", "goodwill_and_other_intangible_assets", schema="stocks"
    )
    op.drop_column("balance_sheet", "other_intangible_assets", schema="stocks")
    op.drop_column("balance_sheet", "goodwill", schema="stocks")
    op.drop_column("balance_sheet", "net_ppe", schema="stocks")
    op.drop_column("balance_sheet", "accumulated_depreciation", schema="stocks")
    op.drop_column("balance_sheet", "gross_ppe", schema="stocks")
    op.drop_column("balance_sheet", "machinery_furniture_equipment", schema="stocks")
    op.drop_column("balance_sheet", "buildings_and_improvements", schema="stocks")
    op.drop_column("balance_sheet", "land_and_improvements", schema="stocks")
    op.drop_column("balance_sheet", "properties", schema="stocks")
    op.drop_column("balance_sheet", "current_assets", schema="stocks")
    op.drop_column("balance_sheet", "other_current_assets", schema="stocks")
    op.drop_column("balance_sheet", "inventory", schema="stocks")
    op.drop_column("balance_sheet", "finished_goods", schema="stocks")
    op.drop_column("balance_sheet", "raw_materials", schema="stocks")
    op.drop_column("balance_sheet", "receivables", schema="stocks")
    op.drop_column("balance_sheet", "accounts_receivable", schema="stocks")
    op.drop_column(
        "balance_sheet",
        "cash_cash_equivalents_and_short_term_investments",
        schema="stocks",
    )
    op.drop_column("balance_sheet", "other_short_term_investments", schema="stocks")
    op.drop_column("balance_sheet", "cash_and_cash_equivalents", schema="stocks")
