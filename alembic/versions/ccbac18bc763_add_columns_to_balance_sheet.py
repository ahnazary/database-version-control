"""Add columns to balance sheet

Revision ID: ccbac18bc763
Revises: f5c7e11c725f
Create Date: 2024-01-04 23:46:48.531280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccbac18bc763'
down_revision: Union[str, None] = 'f5c7e11c725f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
