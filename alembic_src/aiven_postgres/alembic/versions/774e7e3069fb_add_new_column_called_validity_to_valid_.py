"""add new column called validity to valid_tickers table

Revision ID: 774e7e3069fb
Revises: dacd323cc69b
Create Date: 2025-02-07 11:46:12.532370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '774e7e3069fb'
down_revision: Union[str, None] = 'dacd323cc69b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("valid_tickers", sa.Column("validity", sa.Boolean(), nullable=True), schema="finance")


def downgrade() -> None:
    op.drop_column("valid_tickers", "validity", schema="finance")
