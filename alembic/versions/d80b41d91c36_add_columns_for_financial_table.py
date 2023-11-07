"""Add columns for financial table

Revision ID: d80b41d91c36
Revises: 3a5561485ac7
Create Date: 2023-11-07 21:53:05.734237

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d80b41d91c36"
down_revision: Union[str, None] = "3a5561485ac7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the folowing columns to the financials table:
    # otherunder_preferred_stock_dividend 
    # other_special_charges 
    # restructuring_and_mergern_acquisition 
    # general_and_administrative_expense 
    # other_gand_a 
    # salaries_and_wages 

    op.add_column(
        "financials",
        sa.Column(
            "otherunder_preferred_stock_dividend",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "financials",
        sa.Column(
            "other_special_charges",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "financials",
        sa.Column(
            "restructuring_and_mergern_acquisition",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "financials",
        sa.Column(
            "general_and_administrative_expense",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "financials",
        sa.Column(
            "other_gand_a",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )
    op.add_column(
        "financials",
        sa.Column(
            "salaries_and_wages",
            sa.Float(),
            nullable=True,
            server_default=None,
        ),
        schema="stocks",
    )


def downgrade() -> None:
    # Drop the folowing columns from the financials table:
    # otherunder_preferred_stock_dividend 
    # other_special_charges 
    # restructuring_and_mergern_acquisition 
    # general_and_administrative_expense 
    # other_gand_a 
    # salaries_and_wages 

    op.drop_column("financials", "otherunder_preferred_stock_dividend", schema="stocks")
    op.drop_column("financials", "other_special_charges", schema="stocks")
    op.drop_column("financials", "restructuring_and_mergern_acquisition", schema="stocks")
    op.drop_column("financials", "general_and_administrative_expense", schema="stocks")
    op.drop_column("financials", "other_gand_a", schema="stocks")
    op.drop_column("financials", "salaries_and_wages", schema="stocks")
