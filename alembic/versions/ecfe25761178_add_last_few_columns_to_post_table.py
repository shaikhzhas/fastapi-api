"""add last few columns to post table

Revision ID: ecfe25761178
Revises: 771b974346a0
Create Date: 2021-12-16 15:29:49.935953

"""
from datetime import time
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecfe25761178'
down_revision = '771b974346a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')