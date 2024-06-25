"""Remove unique constraint from rut column in Emprendimiento

Revision ID: 5115e48456fd
Revises: 3615f05f8c87
Create Date: 2024-06-04 09:39:08.263111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5115e48456fd'
down_revision = '3615f05f8c87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emprendimiento', schema=None) as batch_op:
        batch_op.alter_column('run',
               existing_type=sa.VARCHAR(length=12),
               nullable=True)
        batch_op.alter_column('rut',
               existing_type=sa.VARCHAR(length=12),
               nullable=True)
        batch_op.alter_column('nombre_emprendimiento',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('razon_social',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('nombre_representante',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('correo_electronico',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('provincia',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('comuna',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('estado',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=5),
               nullable=True)
        batch_op.drop_constraint('emprendimiento_rut_key', type_='unique')
        batch_op.create_unique_constraint(None, ['run'])
        batch_op.drop_column('productos')
        batch_op.drop_column('logo')
        batch_op.drop_column('resena')
        batch_op.drop_column('redes_sociales')
        batch_op.drop_column('video')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emprendimiento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('video', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('redes_sociales', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('resena', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('logo', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('productos', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('emprendimiento_rut_key', ['rut'])
        batch_op.alter_column('estado',
               existing_type=sa.String(length=5),
               type_=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('comuna',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('provincia',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('correo_electronico',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('nombre_representante',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('razon_social',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.alter_column('nombre_emprendimiento',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('rut',
               existing_type=sa.VARCHAR(length=12),
               nullable=False)
        batch_op.alter_column('run',
               existing_type=sa.VARCHAR(length=12),
               nullable=False)

    # ### end Alembic commands ###
