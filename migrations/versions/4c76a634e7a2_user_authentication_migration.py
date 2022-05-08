"""User Authentication Migration

Revision ID: 4c76a634e7a2
Revises: 455e32fd0746
Create Date: 2022-05-08 14:43:14.791627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c76a634e7a2'
down_revision = '455e32fd0746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_hash')
    # ### end Alembic commands ###
