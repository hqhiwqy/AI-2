"""empty message

Revision ID: bf0fb6c17efb
Revises: b78654be7d0a
Create Date: 2020-09-09 16:48:27.827451

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf0fb6c17efb'
down_revision = 'b78654be7d0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=False)
    # ### end Alembic commands ###
