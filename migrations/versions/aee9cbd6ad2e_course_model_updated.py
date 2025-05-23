"""course model updated

Revision ID: aee9cbd6ad2e
Revises: 679759dad7fd
Create Date: 2025-05-23 17:45:48.285613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aee9cbd6ad2e'
down_revision = '679759dad7fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_student_student_number', ['student_number'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint('uq_student_student_number', type_='unique')

    # ### end Alembic commands ###
