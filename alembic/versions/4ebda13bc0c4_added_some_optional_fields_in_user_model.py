"""Added some  optional fields in user model

Revision ID: 4ebda13bc0c4
Revises: 0ad29155fcf1
Create Date: 2025-01-01 19:00:08.563616

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ebda13bc0c4'
down_revision: Union[str, None] = '0ad29155fcf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'is_verfiied',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'is_verfiied',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
