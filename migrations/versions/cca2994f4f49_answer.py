"""answer

Revision ID: cca2994f4f49
Revises: 23c9fc8eadc5
Create Date: 2024-04-27 13:22:38.013882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cca2994f4f49'
down_revision = '23c9fc8eadc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer', sa.String(), nullable=False))
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('answer')

    # ### end Alembic commands ###