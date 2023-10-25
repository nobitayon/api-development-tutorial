"""add user table

Revision ID: 60654f3f84f4
Revises: b8319e979b4c
Create Date: 2023-10-25 15:18:46.216367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60654f3f84f4'
down_revision: Union[str, None] = 'b8319e979b4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column('password',sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade() -> None:
    op.drop_table("users")
