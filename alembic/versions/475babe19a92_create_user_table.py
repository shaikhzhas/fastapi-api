"""create user table

Revision ID: 475babe19a92
Revises: 34aa3e6ba448
Create Date: 2021-12-16 15:15:57.153908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475babe19a92'
down_revision = '34aa3e6ba448'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
