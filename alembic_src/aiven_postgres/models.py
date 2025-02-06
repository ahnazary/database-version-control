from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    Float,
    MetaData,
    Numeric,
    PrimaryKeyConstraint,
    String,
    func,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema="finance"))


class ValidTicker(Base):
    __tablename__ = "valid_tickers"
    __table_args__ = {"schema": "stocks"}

    ticker = Column(String(100), primary_key=True)
    date = Column(Date, default=func.now(), nullable=False)
    currency_code = Column(String(100))
    market_cap = Column(BigInteger)
    total_revenue = Column(BigInteger)
    free_cash_flow = Column(BigInteger)
    total_assets = Column(BigInteger)
    validity = Column(Boolean, nullable=False)


class TickersList(Base):
    __tablename__ = "tickers_list"
    __table_args__ = (PrimaryKeyConstraint("ticker"), {"schema": "stocks"})

    ticker = Column(String, nullable=False)
    name = Column(String)
    exchange = Column(String)
    category_name = Column(String)
    country = Column(String)


class IncomeStatement(Base):
    __tablename__ = "income_stmt"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "report_date", "frequency"),
        {"schema": "stocks"},
    )

    ticker = Column(String(100), nullable=False)
    insert_date = Column(Date, nullable=False, default=func.now())
    report_date = Column(Date, nullable=False)
    currency_code = Column(String(10))
    frequency = Column(String(10), nullable=False)
    tax_effect_of_unusual_items = Column(Float)
    tax_rate_for_calcs = Column(Float)
    normalized_ebitda = Column(Float)
    net_income_from_continuing_operation_net_minority_interest = Column(Float)
    reconciled_depreciation = Column(Float)
    reconciled_cost_of_revenue = Column(Float)
    ebit = Column(Float)
    net_interest_income = Column(Float)
    interest_expense = Column(Float)
    interest_income = Column(Float)
    normalized_income = Column(Float)
    net_income_from_continuing_and_discontinued_operation = Column(Float)
    total_expenses = Column(Float)
    total_operating_income_as_reported = Column(Float)
    diluted_ni_availto_com_stockholders = Column(Float)
    net_income_common_stockholders = Column(Float)
    net_income = Column(Float)
    net_income_including_noncontrolling_interests = Column(Float)
    net_income_continuous_operations = Column(Float)
    tax_provision = Column(Float)
    pretax_income = Column(Float)
    other_income_expense = Column(Float)
    other_non_operating_income_expenses = Column(Float)
    net_non_operating_interest_income_expense = Column(Float)
    interest_expense_non_operating = Column(Float)
    interest_income_non_operating = Column(Float)
    operating_income = Column(Float)
    operating_expense = Column(Float)
    research_and_development = Column(Float)
    selling_general_and_administration = Column(Float)
    gross_profit = Column(Float)
    cost_of_revenue = Column(Float)
    total_revenue = Column(Float)
    operating_revenue = Column(Float)
    diluted_average_shares = Column(Float)
    basic_average_shares = Column(Float)
    total_unusual_items = Column(Float)
    total_unusual_items_excluding_goodwill = Column(Float)
    diluted_eps = Column(Float)
    basic_eps = Column(Float)
    minority_interests = Column(Float)
    special_income_charges = Column(Float)
    gain_on_sale_of_ppe = Column(Float)
    restructuring_and_merger_and_acquisition = Column(Float)
    earnings_from_equity_interest = Column(Float)
    gain_on_sale_of_security = Column(Float)
    other_operating_expenses = Column(Float)
    restructuring_and_mergern_acquisition = Column(Float)
    average_dilution_earnings = Column(Float)
    preferred_stock_dividends = Column(Float)
    net_income_discontinuous_operations = Column(Float)
    impairment_of_capital_assets = Column(Float)
    depreciation_amortization_depletion_income_statement = Column(Float)
    depreciation_and_amortization_in_income_statement = Column(Float)
    otherunder_preferred_stock_dividend = Column(Float)
    selling_and_marketing_expense = Column(Float)
    general_and_administrative_expense = Column(Float)
    other_special_charges = Column(Float)
    write_off = Column(Float)
    total_other_finance_cost = Column(Float)
    amortization = Column(Float)
    amortization_of_intangibles_income_statement = Column(Float)
    other_gand_a = Column(Float)
    salaries_and_wages = Column(Float)
    excise_taxes = Column(Float)


class Financials(Base):
    __tablename__ = "financials"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "report_date", "frequency"),
        {"schema": "stocks"},
    )

    ticker = Column(String(100), nullable=False)
    insert_date = Column(Date, nullable=False, default=func.now())
    report_date = Column(Date, nullable=False)
    currency_code = Column(String(10))
    frequency = Column(String(10), nullable=False)
    tax_effect_of_unusual_items = Column(Float)
    tax_rate_for_calcs = Column(Float)
    normalized_ebitda = Column(Float)
    net_income_from_continuing_operation_net_minority_interest = Column(Float)
    reconciled_depreciation = Column(Float)
    reconciled_cost_of_revenue = Column(Float)
    ebitda = Column(Float)
    ebit = Column(Float)
    net_interest_income = Column(Float)
    interest_expense = Column(Float)
    interest_income = Column(Float)
    normalized_income = Column(Float)
    net_income_from_continuing_and_discontinued_operation = Column(Float)
    total_expenses = Column(Float)
    total_operating_income_as_reported = Column(Float)
    diluted_average_shares = Column(Float)
    basic_average_shares = Column(Float)
    diluted_eps = Column(Float)
    basic_eps = Column(Float)
    diluted_ni_availto_com_stockholders = Column(Float)
    net_income_common_stockholders = Column(Float)
    net_income = Column(Float)
    net_income_including_noncontrolling_interests = Column(Float)
    net_income_continuous_operations = Column(Float)
    tax_provision = Column(Float)
    pretax_income = Column(Float)
    other_income_expense = Column(Float)
    other_non_operating_income_expenses = Column(Float)
    net_non_operating_interest_income_expense = Column(Float)
    interest_expense_non_operating = Column(Float)
    interest_income_non_operating = Column(Float)
    operating_income = Column(Float)
    operating_expense = Column(Float)
    research_and_development = Column(Float)
    selling_general_and_administration = Column(Float)
    gross_profit = Column(Float)
    cost_of_revenue = Column(Float)
    total_revenue = Column(Float)
    operating_revenue = Column(Float)


class Cashflow(Base):
    __tablename__ = "cashflow"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "report_date", "frequency"),
        {"schema": "stocks"},
    )

    ticker = Column(String, primary_key=True, nullable=False)
    insert_date = Column(Date, nullable=False, default="now()")
    report_date = Column(Date, primary_key=True, nullable=False)
    currency_code = Column(String)
    frequency = Column(String(10), primary_key=True, nullable=False)
    free_cash_flow = Column(Float)
    repurchase_of_capital_stock = Column(Float)
    repayment_of_debt = Column(Float)
    issuance_of_debt = Column(Float)
    issuance_of_capital_stock = Column(Float)
    capital_expenditure = Column(Float)
    interest_paid_supplemental_data = Column(Float)
    income_tax_paid_supplemental_data = Column(Float)
    end_cash_position = Column(Float)
    beginning_cash_position = Column(Float)
    changes_in_cash = Column(Float)
    financing_cash_flow = Column(Float)
    cash_flow_from_continuing_financing_activities = Column(Float)
    net_other_financing_charges = Column(Float)
    cash_dividends_paid = Column(Float)
    common_stock_dividend_paid = Column(Float)
    net_common_stock_issuance = Column(Float)
    common_stock_payments = Column(Float)
    common_stock_issuance = Column(Float)
    net_issuance_payments_of_debt = Column(Float)
    net_short_term_debt_issuance = Column(Float)
    short_term_debt_payments = Column(Float)
    short_term_debt_issuance = Column(Float)
    net_long_term_debt_issuance = Column(Float)
    long_term_debt_payments = Column(Float)
    long_term_debt_issuance = Column(Float)
    investing_cash_flow = Column(Float)
    cash_flow_from_continuing_investing_activities = Column(Float)
    net_other_investing_changes = Column(Float)
    net_investment_purchase_and_sale = Column(Float)
    sale_of_investment = Column(Float)
    purchase_of_investment = Column(Float)
    net_business_purchase_and_sale = Column(Float)
    purchase_of_business = Column(Float)
    net_ppe_purchase_and_sale = Column(Float)
    purchase_of_ppe = Column(Float)
    operating_cash_flow = Column(Float)
    cash_flow_from_continuing_operating_activities = Column(Float)
    change_in_working_capital = Column(Float)
    change_in_other_working_capital = Column(Float)
    change_in_other_current_liabilities = Column(Float)
    change_in_other_current_assets = Column(Float)
    change_in_payables_and_accrued_expense = Column(Float)
    change_in_payable = Column(Float)
    change_in_account_payable = Column(Float)
    change_in_inventory = Column(Float)
    change_in_receivables = Column(Float)
    changes_in_account_receivables = Column(Float)
    other_non_cash_items = Column(Float)
    stock_based_compensation = Column(Float)
    deferred_tax = Column(Float)
    deferred_income_tax = Column(Float)
    depreciation_amortization_depletion = Column(Float)
    depreciation_and_amortization = Column(Float)
    net_income_from_continuing_operations = Column(Float)
    cash_from_discontinued_financing_activities = Column(Float)
    dividends_received_cfi = Column(Float)
    sale_of_business = Column(Float)
    capital_expenditure_reported = Column(Float)
    cash_from_discontinued_operating_activities = Column(Float)
    provisionand_write_offof_assets = Column(Float)
    asset_impairment_charge = Column(Float)
    operating_gains_losses = Column(Float)
    pension_and_employee_benefit_expense = Column(Float)
    gain_loss_on_investment_securities = Column(Float)
    effect_of_exchange_rate_changes = Column(Float)
    change_in_accrued_expense = Column(Float)
    change_in_tax_payable = Column(Float)
    change_in_income_tax_payable = Column(Float)
    amortization_cash_flow = Column(Float)
    amortization_of_intangibles = Column(Float)
    depreciation = Column(Float)


class BalanceSheet(Base):
    __tablename__ = "balance_sheet"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "report_date", "frequency"),
        {"schema": "stocks"},
    )

    ticker = Column(String, primary_key=True, nullable=False)
    insert_date = Column(Date, nullable=False, default="now()")
    report_date = Column(Date, nullable=False)
    currency_code = Column(String)
    frequency = Column(String(10), nullable=False)
    ordinary_shares_number = Column(Numeric)
    share_issued = Column(Numeric)
    net_debt = Column(Numeric)
    total_debt = Column(Numeric)
    tangible_book_value = Column(Numeric)
    invested_capital = Column(Numeric)
    working_capital = Column(Numeric)
    net_tangible_assets = Column(Numeric)
    common_stock_equity = Column(Numeric)
    total_capitalization = Column(Numeric)
    total_equity_gross_minority_interest = Column(Numeric)
    stockholders_equity = Column(Numeric)
    gains_losses_not_affecting_retained_earnings = Column(Numeric)
    other_equity_adjustments = Column(Numeric)
    retained_earnings = Column(Numeric)
    additional_paid_in_capital = Column(Numeric)
    capital_stock = Column(Numeric)
    common_stock = Column(Numeric)
    preferred_stock = Column(Numeric)
    total_liabilities_net_minority_interest = Column(Numeric)
    total_non_current_liabilities_net_minority_interest = Column(Numeric)
    other_non_current_liabilities = Column(Numeric)
    employee_benefits = Column(Numeric)
    non_current_pension_and_other_postretirement_benefit_plans = Column(Numeric)
    long_term_debt_and_capital_lease_obligation = Column(Numeric)
    long_term_debt = Column(Numeric)
    current_liabilities = Column(Numeric)
    current_deferred_liabilities = Column(Numeric)
    current_deferred_revenue = Column(Numeric)
    current_debt_and_capital_lease_obligation = Column(Numeric)
    current_debt = Column(Numeric)
    commercial_paper = Column(Numeric)
    pensionand_other_post_retirement_benefit_plans_current = Column(Numeric)
    payables_and_accrued_expenses = Column(Numeric)
    current_accrued_expenses = Column(Numeric)
    payables = Column(Numeric)
    accounts_payable = Column(Numeric)
    total_assets = Column(Numeric)
    total_non_current_assets = Column(Numeric)
    other_non_current_assets = Column(Numeric)
    investments_and_advances = Column(Numeric)
    goodwill_and_other_intangible_assets = Column(Numeric)
    other_intangible_assets = Column(Numeric)
    goodwill = Column(Numeric)
    net_ppe = Column(Numeric)
    accumulated_depreciation = Column(Numeric)
    gross_ppe = Column(Numeric)
    machinery_furniture_equipment = Column(Numeric)
    buildings_and_improvements = Column(Numeric)
    land_and_improvements = Column(Numeric)
    properties = Column(Numeric)
    current_assets = Column(Numeric)
    other_current_assets = Column(Numeric)
    inventory = Column(Numeric)
    finished_goods = Column(Numeric)
    raw_materials = Column(Numeric)
    receivables = Column(Numeric)
    accounts_receivable = Column(Numeric)
    cash_cash_equivalents_and_short_term_investments = Column(Numeric)
    other_short_term_investments = Column(Numeric)
    cash_and_cash_equivalents = Column(Numeric)
    capital_lease_obligations = Column(Numeric)
    fixed_assets_revaluation_reserve = Column(Numeric)
    non_current_deferred_revenue = Column(Numeric)
    long_term_capital_lease_obligation = Column(Numeric)
    current_capital_lease_obligation = Column(Numeric)
    other_payable = Column(Numeric)
    total_tax_payable = Column(Numeric)
    investmentin_financial_assets = Column(Numeric)
    long_term_equity_investment = Column(Numeric)
    investmentsin_associatesat_cost = Column(Numeric)
    other_properties = Column(Numeric)
    hedging_assets_current = Column(Numeric)
    other_receivables = Column(Numeric)
    cash_financial = Column(Numeric)
    preferred_shares_number = Column(Float)
    preferred_stock_equity = Column(Float)
    dividends_payable = Column(Float)
    available_for_sale_securities = Column(Float)
    cash_equivalents = Column(Float)
    treasury_shares_number = Column(Float)
    treasury_stock = Column(Float)
    non_current_deferred_taxes_liabilities = Column(Float)
    other_current_liabilities = Column(Float)
    investment_properties = Column(Float)
    current_deferred_assets = Column(Float)
    prepaid_assets = Column(Float)
    taxes_receivable = Column(Float)
    allowance_for_doubtful_accounts_receivable = Column(Float)
    gross_accounts_receivable = Column(Float)
