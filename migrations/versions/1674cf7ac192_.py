"""empty message

Revision ID: 1674cf7ac192
Revises: 83f14917ad8a
Create Date: 2018-03-31 14:48:46.462982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1674cf7ac192'
down_revision = '83f14917ad8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('additemmodel', sa.Column('recipient_number', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('additemmodel', 'recipient_number')
    # ### end Alembic commands ###
