"""add description

Revision ID: 082d2ac90abc
Revises: 620a637bdbe8
Create Date: 2024-10-27 15:15:07.817012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '082d2ac90abc'
down_revision: Union[str, None] = '620a637bdbe8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_orders_description',
    sa.Column('task_id', sa.BigInteger(), nullable=False),
    sa.Column('food_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('task_id', 'food_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food_orders_description')
    # ### end Alembic commands ###
