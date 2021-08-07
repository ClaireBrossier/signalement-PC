"""admin_user -> user

Revision ID: 07fb827c679a
Revises: 85bc059166cb
Create Date: 2021-08-07 19:35:12.935951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '07fb827c679a'
down_revision = '85bc059166cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='admin_user')
    op.drop_index('name', table_name='admin_user')
    op.drop_table('admin_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=False),
    sa.Column('phone', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('password', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=200), nullable=False),
    sa.Column('role_code', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'admin_user', ['name'], unique=False)
    op.create_index('email', 'admin_user', ['email'], unique=False)
    # ### end Alembic commands ###
