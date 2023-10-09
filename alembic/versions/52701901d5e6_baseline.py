"""Baseline

Revision ID: 52701901d5e6
Revises: 
Create Date: 2023-10-09 23:48:46.563222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52701901d5e6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balance_sheet',
    sa.Column('ticker', sa.String(length=100), nullable=False),
    sa.Column('insert_date', sa.Date(), nullable=False),
    sa.Column('report_date', sa.Date(), nullable=False),
    sa.Column('currency_code', sa.String(length=10), nullable=True),
    sa.Column('frequency', sa.String(length=10), nullable=False),
    sa.Column('Ordinary_Shares_Number', sa.Float(), nullable=True),
    sa.Column('Share_Issued', sa.Float(), nullable=True),
    sa.Column('Net_Debt', sa.Float(), nullable=True),
    sa.Column('Total_Debt', sa.Float(), nullable=True),
    sa.Column('Tangible_Book_Value', sa.Float(), nullable=True),
    sa.Column('Invested_Capital', sa.Float(), nullable=True),
    sa.Column('Working_Capital', sa.Float(), nullable=True),
    sa.Column('Net_Tangible_Assets', sa.Float(), nullable=True),
    sa.Column('Common_Stock_Equity', sa.Float(), nullable=True),
    sa.Column('Total_Capitalization', sa.Float(), nullable=True),
    sa.Column('Total_Equity_Gross_Minority_Interest', sa.Float(), nullable=True),
    sa.Column('Stockholders_Equity', sa.Float(), nullable=True),
    sa.Column('Gains_Losses_Not_Affecting_Retained_Earnings', sa.Float(), nullable=True),
    sa.Column('Retained_Earnings', sa.Float(), nullable=True),
    sa.Column('Capital_Stock', sa.Float(), nullable=True),
    sa.Column('Common_Stock', sa.Float(), nullable=True),
    sa.Column('Total_Liabilities_Net_Minority_Interest', sa.Float(), nullable=True),
    sa.Column('Total_Non_Current_Liabilities_Net_Minority_Interest', sa.Float(), nullable=True),
    sa.Column('Other_Non_Current_Liabilities', sa.Float(), nullable=True),
    sa.Column('Tradeand_Other_Payables_Non_Current', sa.Float(), nullable=True),
    sa.Column('Long_Term_Debt_And_Capital_Lease_Obligation', sa.Float(), nullable=True),
    sa.Column('Long_Term_Debt', sa.Float(), nullable=True),
    sa.Column('Current_Liabilities', sa.Float(), nullable=True),
    sa.Column('Other_Current_Liabilities', sa.Float(), nullable=True),
    sa.Column('Current_Deferred_Liabilities', sa.Float(), nullable=True),
    sa.Column('Current_Deferred_Revenue', sa.Float(), nullable=True),
    sa.Column('Current_Debt_And_Capital_Lease_Obligation', sa.Float(), nullable=True),
    sa.Column('Current_Debt', sa.Float(), nullable=True),
    sa.Column('Other_Current_Borrowings', sa.Float(), nullable=True),
    sa.Column('Commercial_Paper', sa.Float(), nullable=True),
    sa.Column('Payables_And_Accrued_Expenses', sa.Float(), nullable=True),
    sa.Column('Payables', sa.Float(), nullable=True),
    sa.Column('Accounts_Payable', sa.Float(), nullable=True),
    sa.Column('Total_Assets', sa.Float(), nullable=True),
    sa.Column('Total_Non_Current_Assets', sa.Float(), nullable=True),
    sa.Column('Other_Non_Current_Assets', sa.Float(), nullable=True),
    sa.Column('Investments_And_Advances', sa.Float(), nullable=True),
    sa.Column('Other_Investments', sa.Float(), nullable=True),
    sa.Column('Investmentin_Financial_Assets', sa.Float(), nullable=True),
    sa.Column('Available_For_Sale_Securities', sa.Float(), nullable=True),
    sa.Column('Net_PPE', sa.Float(), nullable=True),
    sa.Column('Accumulated_Depreciation', sa.Float(), nullable=True),
    sa.Column('Gross_PPE', sa.Float(), nullable=True),
    sa.Column('Leases', sa.Float(), nullable=True),
    sa.Column('Machinery_Furniture_Equipment', sa.Float(), nullable=True),
    sa.Column('Land_And_Improvements', sa.Float(), nullable=True),
    sa.Column('Properties', sa.Float(), nullable=True),
    sa.Column('Current_Assets', sa.Float(), nullable=True),
    sa.Column('Other_Current_Assets', sa.Float(), nullable=True),
    sa.Column('Inventory', sa.Float(), nullable=True),
    sa.Column('Receivables', sa.Float(), nullable=True),
    sa.Column('Other_Receivables', sa.Float(), nullable=True),
    sa.Column('Accounts_Receivable', sa.Float(), nullable=True),
    sa.Column('Cash_Cash_Equivalents_And_Short_Term_Investments', sa.Float(), nullable=True),
    sa.Column('Other_Short_Term_Investments', sa.Float(), nullable=True),
    sa.Column('Cash_And_Cash_Equivalents', sa.Float(), nullable=True),
    sa.Column('Cash_Equivalents', sa.Float(), nullable=True),
    sa.Column('Cash_Financial', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker', 'report_date', 'frequency'),
    schema='stocks'
    )
    op.create_table('cashflow',
    sa.Column('ticker', sa.String(length=100), nullable=False),
    sa.Column('insert_date', sa.Date(), nullable=False),
    sa.Column('report_date', sa.Date(), nullable=False),
    sa.Column('currency_code', sa.String(length=10), nullable=True),
    sa.Column('frequency', sa.String(length=10), nullable=False),
    sa.Column('free_cash_flow', sa.Float(), nullable=True),
    sa.Column('repurchase_of_capital_stock', sa.Float(), nullable=True),
    sa.Column('repayment_of_debt', sa.Float(), nullable=True),
    sa.Column('issuance_of_debt', sa.Float(), nullable=True),
    sa.Column('issuance_of_capital_stock', sa.Float(), nullable=True),
    sa.Column('capital_expenditure', sa.Float(), nullable=True),
    sa.Column('interest_paid_supplemental_data', sa.Float(), nullable=True),
    sa.Column('income_tax_paid_supplemental_data', sa.Float(), nullable=True),
    sa.Column('end_cash_position', sa.Float(), nullable=True),
    sa.Column('beginning_cash_position', sa.Float(), nullable=True),
    sa.Column('changes_in_cash', sa.Float(), nullable=True),
    sa.Column('financing_cash_flow', sa.Float(), nullable=True),
    sa.Column('cash_flow_from_continuing_financing_activities', sa.Float(), nullable=True),
    sa.Column('net_other_financing_charges', sa.Float(), nullable=True),
    sa.Column('cash_dividends_paid', sa.Float(), nullable=True),
    sa.Column('common_stock_dividend_paid', sa.Float(), nullable=True),
    sa.Column('net_common_stock_issuance', sa.Float(), nullable=True),
    sa.Column('common_stock_payments', sa.Float(), nullable=True),
    sa.Column('common_stock_issuance', sa.Float(), nullable=True),
    sa.Column('net_issuance_payments_of_debt', sa.Float(), nullable=True),
    sa.Column('net_short_term_debt_issuance', sa.Float(), nullable=True),
    sa.Column('short_term_debt_payments', sa.Float(), nullable=True),
    sa.Column('short_term_debt_issuance', sa.Float(), nullable=True),
    sa.Column('net_long_term_debt_issuance', sa.Float(), nullable=True),
    sa.Column('long_term_debt_payments', sa.Float(), nullable=True),
    sa.Column('long_term_debt_issuance', sa.Float(), nullable=True),
    sa.Column('investing_cash_flow', sa.Float(), nullable=True),
    sa.Column('cash_flow_from_continuing_investing_activities', sa.Float(), nullable=True),
    sa.Column('net_other_investing_changes', sa.Float(), nullable=True),
    sa.Column('net_investment_purchase_and_sale', sa.Float(), nullable=True),
    sa.Column('sale_of_investment', sa.Float(), nullable=True),
    sa.Column('purchase_of_investment', sa.Float(), nullable=True),
    sa.Column('net_business_purchase_and_sale', sa.Float(), nullable=True),
    sa.Column('purchase_of_business', sa.Float(), nullable=True),
    sa.Column('net_ppe_purchase_and_sale', sa.Float(), nullable=True),
    sa.Column('purchase_of_ppe', sa.Float(), nullable=True),
    sa.Column('operating_cash_flow', sa.Float(), nullable=True),
    sa.Column('cash_flow_from_continuing_operating_activities', sa.Float(), nullable=True),
    sa.Column('change_in_working_capital', sa.Float(), nullable=True),
    sa.Column('change_in_other_working_capital', sa.Float(), nullable=True),
    sa.Column('change_in_other_current_liabilities', sa.Float(), nullable=True),
    sa.Column('change_in_other_current_assets', sa.Float(), nullable=True),
    sa.Column('change_in_payables_and_accrued_expense', sa.Float(), nullable=True),
    sa.Column('change_in_payable', sa.Float(), nullable=True),
    sa.Column('change_in_account_payable', sa.Float(), nullable=True),
    sa.Column('change_in_inventory', sa.Float(), nullable=True),
    sa.Column('change_in_receivables', sa.Float(), nullable=True),
    sa.Column('changes_in_account_receivables', sa.Float(), nullable=True),
    sa.Column('other_non_cash_items', sa.Float(), nullable=True),
    sa.Column('stock_based_compensation', sa.Float(), nullable=True),
    sa.Column('deferred_tax', sa.Float(), nullable=True),
    sa.Column('deferred_income_tax', sa.Float(), nullable=True),
    sa.Column('depreciation_amortization_depletion', sa.Float(), nullable=True),
    sa.Column('depreciation_and_amortization', sa.Float(), nullable=True),
    sa.Column('net_income_from_continuing_operations', sa.Float(), nullable=True),
    sa.Column('cash_from_discontinued_financing_activities', sa.Float(), nullable=True),
    sa.Column('dividends_received_cfi', sa.Float(), nullable=True),
    sa.Column('sale_of_business', sa.Float(), nullable=True),
    sa.Column('capital_expenditure_reported', sa.Float(), nullable=True),
    sa.Column('cash_from_discontinued_operating_activities', sa.Float(), nullable=True),
    sa.Column('provisionand_write_offof_assets', sa.Float(), nullable=True),
    sa.Column('asset_impairment_charge', sa.Float(), nullable=True),
    sa.Column('operating_gains_losses', sa.Float(), nullable=True),
    sa.Column('pension_and_employee_benefit_expense', sa.Float(), nullable=True),
    sa.Column('gain_loss_on_investment_securities', sa.Float(), nullable=True),
    sa.Column('effect_of_exchange_rate_changes', sa.Float(), nullable=True),
    sa.Column('change_in_accrued_expense', sa.Float(), nullable=True),
    sa.Column('change_in_tax_payable', sa.Float(), nullable=True),
    sa.Column('change_in_income_tax_payable', sa.Float(), nullable=True),
    sa.Column('amortization_cash_flow', sa.Float(), nullable=True),
    sa.Column('amortization_of_intangibles', sa.Float(), nullable=True),
    sa.Column('depreciation', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker', 'report_date', 'frequency'),
    schema='stocks'
    )
    op.create_table('financials',
    sa.Column('ticker', sa.String(length=100), nullable=False),
    sa.Column('insert_date', sa.Date(), nullable=False),
    sa.Column('report_date', sa.Date(), nullable=False),
    sa.Column('currency_code', sa.String(length=10), nullable=True),
    sa.Column('frequency', sa.String(length=10), nullable=False),
    sa.Column('tax_effect_of_unusual_items', sa.Float(), nullable=True),
    sa.Column('tax_rate_for_calcs', sa.Float(), nullable=True),
    sa.Column('normalized_ebitda', sa.Float(), nullable=True),
    sa.Column('net_income_from_continuing_operation_net_minority_interest', sa.Float(), nullable=True),
    sa.Column('reconciled_depreciation', sa.Float(), nullable=True),
    sa.Column('reconciled_cost_of_revenue', sa.Float(), nullable=True),
    sa.Column('ebitda', sa.Float(), nullable=True),
    sa.Column('ebit', sa.Float(), nullable=True),
    sa.Column('net_interest_income', sa.Float(), nullable=True),
    sa.Column('interest_expense', sa.Float(), nullable=True),
    sa.Column('interest_income', sa.Float(), nullable=True),
    sa.Column('normalized_income', sa.Float(), nullable=True),
    sa.Column('net_income_from_continuing_and_discontinued_operation', sa.Float(), nullable=True),
    sa.Column('total_expenses', sa.Float(), nullable=True),
    sa.Column('total_operating_income_as_reported', sa.Float(), nullable=True),
    sa.Column('diluted_average_shares', sa.Float(), nullable=True),
    sa.Column('basic_average_shares', sa.Float(), nullable=True),
    sa.Column('diluted_eps', sa.Float(), nullable=True),
    sa.Column('basic_eps', sa.Float(), nullable=True),
    sa.Column('diluted_ni_availto_com_stockholders', sa.Float(), nullable=True),
    sa.Column('net_income_common_stockholders', sa.Float(), nullable=True),
    sa.Column('net_income', sa.Float(), nullable=True),
    sa.Column('net_income_including_noncontrolling_interests', sa.Float(), nullable=True),
    sa.Column('net_income_continuous_operations', sa.Float(), nullable=True),
    sa.Column('tax_provision', sa.Float(), nullable=True),
    sa.Column('pretax_income', sa.Float(), nullable=True),
    sa.Column('other_income_expense', sa.Float(), nullable=True),
    sa.Column('other_non_operating_income_expenses', sa.Float(), nullable=True),
    sa.Column('net_non_operating_interest_income_expense', sa.Float(), nullable=True),
    sa.Column('interest_expense_non_operating', sa.Float(), nullable=True),
    sa.Column('interest_income_non_operating', sa.Float(), nullable=True),
    sa.Column('operating_income', sa.Float(), nullable=True),
    sa.Column('operating_expense', sa.Float(), nullable=True),
    sa.Column('research_and_development', sa.Float(), nullable=True),
    sa.Column('selling_general_and_administration', sa.Float(), nullable=True),
    sa.Column('gross_profit', sa.Float(), nullable=True),
    sa.Column('cost_of_revenue', sa.Float(), nullable=True),
    sa.Column('total_revenue', sa.Float(), nullable=True),
    sa.Column('operating_revenue', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker', 'report_date', 'frequency'),
    schema='stocks'
    )
    op.create_table('income_stmt',
    sa.Column('ticker', sa.String(length=100), nullable=False),
    sa.Column('insert_date', sa.Date(), nullable=False),
    sa.Column('report_date', sa.Date(), nullable=False),
    sa.Column('currency_code', sa.String(length=10), nullable=True),
    sa.Column('frequency', sa.String(length=10), nullable=False),
    sa.Column('tax_effect_of_unusual_items', sa.Float(), nullable=True),
    sa.Column('tax_rate_for_calcs', sa.Float(), nullable=True),
    sa.Column('normalized_ebitda', sa.Float(), nullable=True),
    sa.Column('net_income_from_continuing_operation_net_minority_interest', sa.Float(), nullable=True),
    sa.Column('reconciled_depreciation', sa.Float(), nullable=True),
    sa.Column('reconciled_cost_of_revenue', sa.Float(), nullable=True),
    sa.Column('ebit', sa.Float(), nullable=True),
    sa.Column('net_interest_income', sa.Float(), nullable=True),
    sa.Column('interest_expense', sa.Float(), nullable=True),
    sa.Column('interest_income', sa.Float(), nullable=True),
    sa.Column('normalized_income', sa.Float(), nullable=True),
    sa.Column('net_income_from_continuing_and_discontinued_operation', sa.Float(), nullable=True),
    sa.Column('total_expenses', sa.Float(), nullable=True),
    sa.Column('total_operating_income_as_reported', sa.Float(), nullable=True),
    sa.Column('diluted_ni_availto_com_stockholders', sa.Float(), nullable=True),
    sa.Column('net_income_common_stockholders', sa.Float(), nullable=True),
    sa.Column('net_income', sa.Float(), nullable=True),
    sa.Column('net_income_including_noncontrolling_interests', sa.Float(), nullable=True),
    sa.Column('net_income_continuous_operations', sa.Float(), nullable=True),
    sa.Column('tax_provision', sa.Float(), nullable=True),
    sa.Column('pretax_income', sa.Float(), nullable=True),
    sa.Column('other_income_expense', sa.Float(), nullable=True),
    sa.Column('other_non_operating_income_expenses', sa.Float(), nullable=True),
    sa.Column('net_non_operating_interest_income_expense', sa.Float(), nullable=True),
    sa.Column('interest_expense_non_operating', sa.Float(), nullable=True),
    sa.Column('interest_income_non_operating', sa.Float(), nullable=True),
    sa.Column('operating_income', sa.Float(), nullable=True),
    sa.Column('operating_expense', sa.Float(), nullable=True),
    sa.Column('research_and_development', sa.Float(), nullable=True),
    sa.Column('selling_general_and_administration', sa.Float(), nullable=True),
    sa.Column('gross_profit', sa.Float(), nullable=True),
    sa.Column('cost_of_revenue', sa.Float(), nullable=True),
    sa.Column('total_revenue', sa.Float(), nullable=True),
    sa.Column('operating_revenue', sa.Float(), nullable=True),
    sa.Column('diluted_average_shares', sa.Float(), nullable=True),
    sa.Column('basic_average_shares', sa.Float(), nullable=True),
    sa.Column('total_unusual_items', sa.Float(), nullable=True),
    sa.Column('total_unusual_items_excluding_goodwill', sa.Float(), nullable=True),
    sa.Column('diluted_eps', sa.Float(), nullable=True),
    sa.Column('basic_eps', sa.Float(), nullable=True),
    sa.Column('minority_interests', sa.Float(), nullable=True),
    sa.Column('special_income_charges', sa.Float(), nullable=True),
    sa.Column('gain_on_sale_of_ppe', sa.Float(), nullable=True),
    sa.Column('restructuring_and_merger_and_acquisition', sa.Float(), nullable=True),
    sa.Column('earnings_from_equity_interest', sa.Float(), nullable=True),
    sa.Column('gain_on_sale_of_security', sa.Float(), nullable=True),
    sa.Column('other_operating_expenses', sa.Float(), nullable=True),
    sa.Column('restructuring_and_mergern_acquisition', sa.Float(), nullable=True),
    sa.Column('average_dilution_earnings', sa.Float(), nullable=True),
    sa.Column('preferred_stock_dividends', sa.Float(), nullable=True),
    sa.Column('net_income_discontinuous_operations', sa.Float(), nullable=True),
    sa.Column('impairment_of_capital_assets', sa.Float(), nullable=True),
    sa.Column('depreciation_amortization_depletion_income_statement', sa.Float(), nullable=True),
    sa.Column('depreciation_and_amortization_in_income_statement', sa.Float(), nullable=True),
    sa.Column('otherunder_preferred_stock_dividend', sa.Float(), nullable=True),
    sa.Column('selling_and_marketing_expense', sa.Float(), nullable=True),
    sa.Column('general_and_administrative_expense', sa.Float(), nullable=True),
    sa.Column('other_special_charges', sa.Float(), nullable=True),
    sa.Column('write_off', sa.Float(), nullable=True),
    sa.Column('total_other_finance_cost', sa.Float(), nullable=True),
    sa.Column('amortization', sa.Float(), nullable=True),
    sa.Column('amortization_of_intangibles_income_statement', sa.Float(), nullable=True),
    sa.Column('other_gand_a', sa.Float(), nullable=True),
    sa.Column('salaries_and_wages', sa.Float(), nullable=True),
    sa.Column('excise_taxes', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker', 'report_date', 'frequency'),
    schema='stocks'
    )
    op.create_table('tickers_list',
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('category_name', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ticker'),
    schema='stocks'
    )
    op.create_table('valid_tickers',
    sa.Column('ticker', sa.String(length=100), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('currency_code', sa.String(length=100), nullable=True),
    sa.Column('market_cap', sa.BigInteger(), nullable=True),
    sa.Column('total_revenue', sa.BigInteger(), nullable=True),
    sa.Column('free_cash_flow', sa.BigInteger(), nullable=True),
    sa.Column('total_assets', sa.BigInteger(), nullable=True),
    sa.Column('validity', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('ticker'),
    schema='stocks'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('valid_tickers', schema='stocks')
    op.drop_table('tickers_list', schema='stocks')
    op.drop_table('income_stmt', schema='stocks')
    op.drop_table('financials', schema='stocks')
    op.drop_table('cashflow', schema='stocks')
    op.drop_table('balance_sheet', schema='stocks')
    # ### end Alembic commands ###
