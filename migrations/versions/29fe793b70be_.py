"""empty message

Revision ID: 29fe793b70be
Revises: c02d445cd96e
Create Date: 2023-12-05 09:23:04.056229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29fe793b70be'
down_revision = 'c02d445cd96e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ts_ticket', schema=None) as batch_op:
        batch_op.alter_column('submission_by',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('process_by',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ts_ticket', schema=None) as batch_op:
        batch_op.alter_column('process_by',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('submission_by',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###
