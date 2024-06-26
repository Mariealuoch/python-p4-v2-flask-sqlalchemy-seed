"""Initial migration

Revision ID: 5392749c0ac6
Revises: 
Create Date: 2024-06-26 12:22:51.041594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5392749c0ac6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
