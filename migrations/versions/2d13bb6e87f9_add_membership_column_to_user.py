"""Add membership column to User

Revision ID: 2d13bb6e87f9
Revises: 
Create Date: 2024-01-27 12:07:06.397839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d13bb6e87f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        op.add_column('user', sa.Column('membership', sa.String(length=255), nullable=False, server_default='Free'))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('membership')

    # ### end Alembic commands ###
