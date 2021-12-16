"""create post table

Revision ID: b799b044b3b2
Revises: 
Create Date: 2021-12-16 15:03:13.371049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b799b044b3b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False,primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('posts')
