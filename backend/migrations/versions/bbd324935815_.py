"""empty message

Revision ID: bbd324935815
Revises: 180f0aabfcd6
Create Date: 2017-04-19 19:48:16.163283

"""

# revision identifiers, used by Alembic.
revision = 'bbd324935815'
down_revision = '180f0aabfcd6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('entries_project_id_fkey', 'entries', type_='foreignkey')
    op.create_foreign_key(None, 'entries', 'projects', ['project_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entries', type_='foreignkey')
    op.create_foreign_key('entries_project_id_fkey', 'entries', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###