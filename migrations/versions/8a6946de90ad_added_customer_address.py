"""Added customer address

Revision ID: 8a6946de90ad
Revises: 1674cf7ac192
Create Date: 2018-04-22 09:41:49.047531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a6946de90ad'
down_revision = '1674cf7ac192'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('additemmodel', sa.Column('address', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('additemmodel', 'address')
    # ### end Alembic commands ###
