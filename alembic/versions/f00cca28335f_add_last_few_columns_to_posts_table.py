"""add last few columns to posts table

Revision ID: f00cca28335f
Revises: f9486aa9d7c6
Create Date: 2023-10-25 15:32:41.557833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f00cca28335f'
down_revision: Union[str, None] = 'f9486aa9d7c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE')),
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
