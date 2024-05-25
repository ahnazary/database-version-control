"""Create NEw schema for dbt models

Revision ID: 49217d5d1147
Revises: c10c28851d50
Create Date: 2024-05-25 11:44:33.729453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49217d5d1147'
down_revision: Union[str, None] = 'c10c28851d50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS dbt_models")


def downgrade() -> None:
    op.execute("DROP SCHEMA IF EXISTS dbt_models")
