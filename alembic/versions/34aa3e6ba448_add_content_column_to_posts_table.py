"""add content column to posts table

Revision ID: 34aa3e6ba448
Revises: b799b044b3b2
Create Date: 2021-12-16 15:10:57.570811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34aa3e6ba448'
down_revision = 'b799b044b3b2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))


def downgrade():
    op.drop_column('posts','content')
