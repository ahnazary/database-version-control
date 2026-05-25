from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    MetaData,
    PrimaryKeyConstraint,
    String,
    func,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData(schema="finance"))


class IncomeStatement(Base):
    __tablename__ = "income_stmt"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "metric", "report_date", "frequency"),
        {"schema": "finance"},
    )

    ticker = Column(String(20), nullable=False)
    frequency = Column(String(10), nullable=False)
    report_date = Column(Date, nullable=False)
    metric = Column(String(100), nullable=False)
    value = Column(Float)
    insert_datetime = Column(DateTime, nullable=False, server_default=func.now())


class CashFlow(Base):
    __tablename__ = "cash_flow"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "metric", "report_date", "frequency"),
        {"schema": "finance"},
    )

    ticker = Column(String(20), nullable=False)
    frequency = Column(String(10), nullable=False)
    report_date = Column(Date, nullable=False)
    metric = Column(String(100), nullable=False)
    value = Column(Float)
    insert_datetime = Column(DateTime, nullable=False, server_default=func.now())


class BalanceSheet(Base):
    __tablename__ = "balance_sheet"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "metric", "report_date", "frequency"),
        {"schema": "finance"},
    )

    ticker = Column(String(20), nullable=False)
    frequency = Column(String(10), nullable=False)
    report_date = Column(Date, nullable=False)
    metric = Column(String(100), nullable=False)
    value = Column(Float)
    insert_datetime = Column(DateTime, nullable=False, server_default=func.now())


class Financials(Base):
    __tablename__ = "financials"
    __table_args__ = (
        PrimaryKeyConstraint("ticker", "metric", "report_date", "frequency"),
        {"schema": "finance"},
    )

    ticker = Column(String(20), nullable=False)
    frequency = Column(String(10), nullable=False)
    report_date = Column(Date, nullable=False)
    metric = Column(String(100), nullable=False)
    value = Column(Float)
    insert_datetime = Column(DateTime, nullable=False, server_default=func.now())


class ActiveTickers(Base):
    __tablename__ = "active_tickers"
    __table_args__ = (
        PrimaryKeyConstraint("ticker"),
        {"schema": "finance"},
    )

    ticker = Column(String(20), nullable=False)
    name = Column(String(200))
    exchange = Column(String(50))
    category_name = Column(String(100))
    country = Column(String(50))
    is_active = Column(Boolean, nullable=False, default=True)
    upsert_datetime = Column(DateTime, nullable=False, server_default=func.now())
