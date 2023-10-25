"""add content column to post table

Revision ID: b8319e979b4c
Revises: 3ada04645fae
Create Date: 2023-10-25 15:16:35.148749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8319e979b4c'
down_revision: Union[str, None] = '3ada04645fae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))

def downgrade() -> None:
    op.drop_column('posts','content')
