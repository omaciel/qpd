"""Add columns to revision table

Revision ID: cc8943b01a5c
Revises: 
Create Date: 2016-12-20 11:40:34.848221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc8943b01a5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('releases', sa.Column('major', sa.Integer, nullable=True))
    op.add_column('releases', sa.Column('minor', sa.Integer, nullable=True))
    op.add_column('releases', sa.Column('patch', sa.Integer, nullable=True))


def downgrade():
    pass
