"""Init

Revision ID: d5a184b84c77
Revises: 76063b4daabc
Create Date: 2024-10-12 12:45:22.255068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5a184b84c77'
down_revision: Union[str, None] = '76063b4daabc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_page_way_page_id', table_name='page_way')
    op.drop_index('ix_page_way_way_id', table_name='page_way')
    op.drop_table('page_way')
    op.add_column('ways', sa.Column('page_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ways', 'pages', ['page_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ways', type_='foreignkey')
    op.drop_column('ways', 'page_id')
    op.create_table('page_way',
    sa.Column('page_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('way_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['pages.id'], name='page_way_page_id_fkey'),
    sa.ForeignKeyConstraint(['way_id'], ['ways.id'], name='page_way_way_id_fkey'),
    sa.PrimaryKeyConstraint('page_id', 'way_id', name='page_way_pkey')
    )
    op.create_index('ix_page_way_way_id', 'page_way', ['way_id'], unique=False)
    op.create_index('ix_page_way_page_id', 'page_way', ['page_id'], unique=False)
    # ### end Alembic commands ###
