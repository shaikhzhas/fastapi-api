"""add foreign key for post table

Revision ID: 771b974346a0
Revises: 475babe19a92
Create Date: 2021-12-16 15:22:04.670973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771b974346a0'
down_revision = '475babe19a92'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key(
        'post_users_fk',
        source_table = 'posts',
        referent_table = 'users',
        local_cols = ['owner_id'],
        remote_cols = ['id'],
        ondelete = 'CASCADE' 
    )

def downgrade():
    op.drop_constraint('post_users_fk', table_name = 'posts')
    op.drop_column('posts','owner_id')

