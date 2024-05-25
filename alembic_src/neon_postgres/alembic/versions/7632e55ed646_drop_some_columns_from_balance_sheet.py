"""Drop some columns from balance_sheet

Revision ID: 7632e55ed646
Revises: 222648ce9bb9
Create Date: 2023-11-13 23:01:59.350923

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7632e55ed646"
down_revision: Union[str, None] = "222648ce9bb9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # drop following columns from balance_sheet table:
    # "Ordinary Shares Number"
    # "Share Issued"
    # "Net Debt"
    # "Total Debt"
    # "Tangible Book Value"
    # "Invested Capital"
    # "Working Capital"
    # "Net Tangible Assets"
    # "Common Stock Equity"
    # "Total Capitalization"
    # "Total Equity Gross Minority Interest"
    # "Stockholders Equity"
    # "Gains Losses Not Affecting Retained Earnings"
    # "Retained Earnings"
    # "Capital Stock"
    # "Common Stock"
    # "Total Liabilities Net Minority Interest"
    # "Total Non Current Liabilities Net Minority Interest"
    # "Other Non Current Liabilities"
    # "Tradeand Other Payables Non Current"
    # "Long Term Debt And Capital Lease Obligation"
    # "Long Term Debt"
    # "Current Liabilities"
    # "Other Current Liabilities"
    # "Current Deferred Liabilities"
    # "Current Deferred Revenue"
    # "Current Debt And Capital Lease Obligation"
    # "Current Debt"
    # "Other Current Borrowings"
    # "Commercial Paper"
    # "Payables And Accrued Expenses"
    # "Payables"
    # "Accounts Payable"
    # "Total Assets"
    # "Total Non Current Assets"
    # "Other Non Current Assets"
    # "Investments And Advances"
    # "Other Investments"
    # "Investmentin Financial Assets"
    # "Available For Sale Securities"
    # "Net PPE"
    # "Accumulated Depreciation"
    # "Gross PPE"
    # "Leases"
    # "Machinery Furniture Equipment"
    # "Land And Improvements"
    # "Properties"
    # "Current Assets"
    # "Other Current Assets"
    # "Inventory"
    # "Receivables"
    # "Other Receivables"
    # "Accounts Receivable"
    # "Cash Cash Equivalents And Short Term Investments"
    # "Other Short Term Investments"
    # "Cash And Cash Equivalents"
    # "Cash Equivalents"
    # "Cash Financial"

    op.drop_column("balance_sheet", "Ordinary Shares Number", schema="stocks")
    op.drop_column("balance_sheet", "Share Issued", schema="stocks")
    op.drop_column("balance_sheet", "Net Debt", schema="stocks")
    op.drop_column("balance_sheet", "Total Debt", schema="stocks")
    op.drop_column("balance_sheet", "Tangible Book Value", schema="stocks")
    op.drop_column("balance_sheet", "Invested Capital", schema="stocks")
    op.drop_column("balance_sheet", "Working Capital", schema="stocks")
    op.drop_column("balance_sheet", "Net Tangible Assets", schema="stocks")
    op.drop_column("balance_sheet", "Common Stock Equity", schema="stocks")
    op.drop_column("balance_sheet", "Total Capitalization", schema="stocks")
    op.drop_column(
        "balance_sheet", "Total Equity Gross Minority Interest", schema="stocks"
    )
    op.drop_column("balance_sheet", "Stockholders Equity", schema="stocks")
    op.drop_column(
        "balance_sheet", "Gains Losses Not Affecting Retained Earnings", schema="stocks"
    )
    op.drop_column("balance_sheet", "Retained Earnings", schema="stocks")
    op.drop_column("balance_sheet", "Capital Stock", schema="stocks")
    op.drop_column("balance_sheet", "Common Stock", schema="stocks")
    op.drop_column(
        "balance_sheet", "Total Liabilities Net Minority Interest", schema="stocks"
    )
    op.drop_column(
        "balance_sheet",
        "Total Non Current Liabilities Net Minority Interest",
        schema="stocks",
    )
    op.drop_column("balance_sheet", "Other Non Current Liabilities", schema="stocks")
    op.drop_column(
        "balance_sheet", "Tradeand Other Payables Non Current", schema="stocks"
    )
    op.drop_column(
        "balance_sheet", "Long Term Debt And Capital Lease Obligation", schema="stocks"
    )
    op.drop_column("balance_sheet", "Long Term Debt", schema="stocks")
    op.drop_column("balance_sheet", "Current Liabilities", schema="stocks")
    op.drop_column("balance_sheet", "Other Current Liabilities", schema="stocks")
    op.drop_column("balance_sheet", "Current Deferred Liabilities", schema="stocks")
    op.drop_column("balance_sheet", "Current Deferred Revenue", schema="stocks")
    op.drop_column(
        "balance_sheet", "Current Debt And Capital Lease Obligation", schema="stocks"
    )
    op.drop_column("balance_sheet", "Current Debt", schema="stocks")
    op.drop_column("balance_sheet", "Other Current Borrowings", schema="stocks")
    op.drop_column("balance_sheet", "Commercial Paper", schema="stocks")
    op.drop_column("balance_sheet", "Payables And Accrued Expenses", schema="stocks")
    op.drop_column("balance_sheet", "Payables", schema="stocks")
    op.drop_column("balance_sheet", "Accounts Payable", schema="stocks")
    op.drop_column("balance_sheet", "Total Assets", schema="stocks")
    op.drop_column("balance_sheet", "Total Non Current Assets", schema="stocks")
    op.drop_column("balance_sheet", "Other Non Current Assets", schema="stocks")
    op.drop_column("balance_sheet", "Investments And Advances", schema="stocks")
    op.drop_column("balance_sheet", "Other Investments", schema="stocks")
    op.drop_column("balance_sheet", "Investmentin Financial Assets", schema="stocks")
    op.drop_column("balance_sheet", "Available For Sale Securities", schema="stocks")
    op.drop_column("balance_sheet", "Net PPE", schema="stocks")
    op.drop_column("balance_sheet", "Accumulated Depreciation", schema="stocks")
    op.drop_column("balance_sheet", "Gross PPE", schema="stocks")
    op.drop_column("balance_sheet", "Leases", schema="stocks")
    op.drop_column("balance_sheet", "Machinery Furniture Equipment", schema="stocks")
    op.drop_column("balance_sheet", "Land And Improvements", schema="stocks")
    op.drop_column("balance_sheet", "Properties", schema="stocks")
    op.drop_column("balance_sheet", "Current Assets", schema="stocks")
    op.drop_column("balance_sheet", "Other Current Assets", schema="stocks")
    op.drop_column("balance_sheet", "Inventory", schema="stocks")
    op.drop_column("balance_sheet", "Receivables", schema="stocks")
    op.drop_column("balance_sheet", "Other Receivables", schema="stocks")
    op.drop_column("balance_sheet", "Accounts Receivable", schema="stocks")
    op.drop_column(
        "balance_sheet",
        "Cash Cash Equivalents And Short Term Investments",
        schema="stocks",
    )
    op.drop_column("balance_sheet", "Other Short Term Investments", schema="stocks")
    op.drop_column("balance_sheet", "Cash And Cash Equivalents", schema="stocks")
    op.drop_column("balance_sheet", "Cash Equivalents", schema="stocks")
    op.drop_column("balance_sheet", "Cash Financial", schema="stocks")


def downgrade() -> None:
    pass
