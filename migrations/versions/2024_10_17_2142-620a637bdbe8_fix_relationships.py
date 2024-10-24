"""fix relationships

Revision ID: 620a637bdbe8
Revises: e57b90c9c8fc
Create Date: 2024-10-17 21:42:58.684404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '620a637bdbe8'
down_revision: Union[str, None] = 'e57b90c9c8fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organizations', sa.Column('owner_id', sa.BigInteger(), nullable=False))
    op.drop_constraint('organizations_owner_fkey', 'organizations', type_='foreignkey')
    op.create_foreign_key(None, 'organizations', 'owners', ['owner_id'], ['id'])
    op.drop_column('organizations', 'owner')
    op.alter_column('tasks', 'worker_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'worker_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.add_column('organizations', sa.Column('owner', sa.BIGINT(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'organizations', type_='foreignkey')
    op.create_foreign_key('organizations_owner_fkey', 'organizations', 'owners', ['owner'], ['id'])
    op.drop_column('organizations', 'owner_id')
    # ### end Alembic commands ###
