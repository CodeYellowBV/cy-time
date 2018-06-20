"""empty message

Revision ID: 4be545224f47
Revises: 0afddd2bad7d
Create Date: 2018-06-15 14:34:01.383921

"""

# revision identifiers, used by Alembic.
revision = '4be545224f47'
down_revision = '0afddd2bad7d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('still_working', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'still_working')
    # ### end Alembic commands ###