"""add foreign key to posts table

Revision ID: f9486aa9d7c6
Revises: 60654f3f84f4
Create Date: 2023-10-25 15:23:08.366249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9486aa9d7c6'
down_revision: Union[str, None] = '60654f3f84f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts", referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
