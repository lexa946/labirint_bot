"""Init

Revision ID: 49c5bd58869d
Revises: 0ddf41d5fa71
Create Date: 2024-10-12 19:35:09.407185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49c5bd58869d'
down_revision: Union[str, None] = '0ddf41d5fa71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('heroes', sa.Column('has_died', sa.Boolean(), nullable=False))
    op.add_column('stuffs', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stuffs', 'is_active')
    op.drop_column('heroes', 'has_died')
    # ### end Alembic commands ###
