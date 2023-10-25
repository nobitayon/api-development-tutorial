"""create posts table

Revision ID: 3ada04645fae
Revises: 
Create Date: 2023-10-25 15:14:48.409529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ada04645fae'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts', 
        sa.Column('id',sa.INTEGER(),nullable=False,primary_key=True),
        sa.Column('title',sa.String(),nullable=False)
    )

def downgrade() -> None:
    op.drop_table('posts')
