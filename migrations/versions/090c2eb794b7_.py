"""empty message

Revision ID: 090c2eb794b7
Revises: 5fe92cb86490
Create Date: 2017-06-30 16:26:01.446791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090c2eb794b7'
down_revision = '5fe92cb86490'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ab_permission')
    op.drop_table('ab_permission_view_role')
    op.drop_table('associations')
    op.drop_table('ab_user_role')
    op.drop_table('ab_role')
    op.drop_table('ab_view_menu')
    op.drop_table('ab_permission_view')
    op.drop_table('ab_register_user')
    op.drop_table('ab_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ab_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), nullable=True),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_login', sa.DATETIME(), nullable=True),
    sa.Column('login_count', sa.INTEGER(), nullable=True),
    sa.Column('fail_login_count', sa.INTEGER(), nullable=True),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('changed_on', sa.DATETIME(), nullable=True),
    sa.Column('created_by_fk', sa.INTEGER(), nullable=True),
    sa.Column('changed_by_fk', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('active IN (0, 1)'),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ab_register_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('registration_date', sa.DATETIME(), nullable=True),
    sa.Column('registration_hash', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ab_permission_view',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('permission_id', sa.INTEGER(), nullable=True),
    sa.Column('view_menu_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['ab_permission.id'], ),
    sa.ForeignKeyConstraint(['view_menu_id'], ['ab_view_menu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_view_menu',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ab_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ab_user_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['ab_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('associations',
    sa.Column('created_on', sa.DATETIME(), nullable=False),
    sa.Column('changed_on', sa.DATETIME(), nullable=False),
    sa.Column('snp_id', sa.VARCHAR(length=16), nullable=False),
    sa.Column('snp_locn_chr', sa.VARCHAR(length=9), nullable=False),
    sa.Column('snp_locn_posn', sa.INTEGER(), nullable=False),
    sa.Column('snp_base_wild', sa.VARCHAR(length=1), nullable=False),
    sa.Column('snp_base_var', sa.VARCHAR(length=1), nullable=False),
    sa.Column('cpg_id', sa.VARCHAR(length=16), nullable=False),
    sa.Column('cpg_locn_chr', sa.VARCHAR(length=9), nullable=False),
    sa.Column('cpg_locn_posn', sa.INTEGER(), nullable=False),
    sa.Column('stat_beta', sa.FLOAT(), nullable=True),
    sa.Column('stat_stderr', sa.FLOAT(), nullable=True),
    sa.Column('stat_pval', sa.FLOAT(), nullable=True),
    sa.Column('created_by_fk', sa.INTEGER(), nullable=False),
    sa.Column('changed_by_fk', sa.INTEGER(), nullable=False),
    sa.CheckConstraint("cpg_locn_chr IN ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'x', 'y')", name='chromosome'),
    sa.CheckConstraint("snp_locn_chr IN ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'x', 'y')", name='chromosome'),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('snp_id', 'cpg_id')
    )
    op.create_table('ab_permission_view_role',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('permission_view_id', sa.INTEGER(), nullable=True),
    sa.Column('role_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['permission_view_id'], ['ab_permission_view.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['ab_role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ab_permission',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###