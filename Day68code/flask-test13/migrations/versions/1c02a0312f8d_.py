"""empty message

Revision ID: 1c02a0312f8d
Revises: cf1c15b842c6
Create Date: 2020-09-10 16:25:33.149991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c02a0312f8d'
down_revision = 'cf1c15b842c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('types', sa.String(length=10), nullable=False),
    sa.Column('img_url', sa.String(length=300), nullable=True),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('is_recommend', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    # ### end Alembic commands ###
