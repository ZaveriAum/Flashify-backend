"""notes table added

Revision ID: cb6db2185c1c
Revises: 5c026882e76b
Create Date: 2025-02-28 01:12:41.615723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb6db2185c1c'
down_revision = '5c026882e76b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('note', sa.Text(), nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['folder_id'], ['folders.id'], name='fk_notes_folders'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    # ### end Alembic commands ###
