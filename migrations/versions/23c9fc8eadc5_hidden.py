"""hidden

Revision ID: 23c9fc8eadc5
Revises: 267777b9be7a
Create Date: 2024-04-27 13:01:45.917301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23c9fc8eadc5'
down_revision = '267777b9be7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan_features', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hidden', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan_features', schema=None) as batch_op:
        batch_op.drop_column('hidden')

    # ### end Alembic commands ###