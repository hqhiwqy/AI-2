"""empty message

Revision ID: df46122d963c
Revises: 1ef18e6158a9
Create Date: 2020-09-08 09:00:12.567159

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'df46122d963c'
down_revision = '1ef18e6158a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'status',
               existing_type=mysql.INTEGER(),
               server_default='1',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'status',
               existing_type=mysql.INTEGER(),
               server_default=sa.text("'0'"),
               existing_nullable=True)
    # ### end Alembic commands ###