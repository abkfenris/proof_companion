"""Initial migration

Revision ID: 88c32538cb1
Revises: None
Create Date: 2015-03-24 22:48:27.982105

"""

# revision identifiers, used by Alembic.
revision = '88c32538cb1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('_created', sa.DateTime(), nullable=True),
    sa.Column('_updated', sa.DateTime(), nullable=True),
    sa.Column('_etag', sa.String(length=40), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('lastname', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    ### end Alembic commands ###
