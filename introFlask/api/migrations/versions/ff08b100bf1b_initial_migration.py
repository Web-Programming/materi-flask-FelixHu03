"""Initial migration

Revision ID: ff08b100bf1b
Revises: 
Create Date: 2024-11-21 19:50:46.027125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff08b100bf1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fakultas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prodi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('fakultas_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fakultas_id'], ['fakultas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mahasiswa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('nim', sa.String(length=20), nullable=False),
    sa.Column('prodi_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['prodi_id'], ['prodi.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nim')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mahasiswa')
    op.drop_table('prodi')
    op.drop_table('fakultas')
    # ### end Alembic commands ###
