"""Init database

Revision ID: 03c9d3e2aa7e
Revises: 
Create Date: 2020-09-30 13:25:43.794080

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = '03c9d3e2aa7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plots',
                    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('cw', sa.String(length=512), nullable=True),
                    sa.Column('local_only', sa.Boolean(), nullable=True),
                    sa.Column('uri', sa.String(length=512), nullable=True),
                    sa.Column('url', sa.String(length=512), nullable=True),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
                    sa.Column('username', sa.String(length=32), nullable=True),
                    sa.Column('display_name', sa.String(length=255), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('is_admin', sa.Boolean(), nullable=True),
                    sa.Column('is_moderator', sa.Boolean(), nullable=True),
                    sa.Column('is_silence', sa.Boolean(), nullable=True),
                    sa.Column('is_suspend', sa.Boolean(), nullable=True),
                    sa.Column('is_bot', sa.Boolean(), nullable=True),
                    sa.Column('is_manual_follow', sa.Boolean(), nullable=True),
                    sa.Column('is_remote_user', sa.Boolean(), nullable=True),
                    sa.Column('remote_host', sa.String(length=255), nullable=True),
                    sa.Column('remote_inbox', sa.String(length=512), nullable=True),
                    sa.Column('remote_share_inbox', sa.String(length=512), nullable=True),
                    sa.Column('remote_outbox', sa.String(length=512), nullable=True),
                    sa.Column('remote_featured', sa.String(length=512), nullable=True),
                    sa.Column('remote_uri', sa.String(length=512), nullable=True),
                    sa.Column('remote_key_id', sa.String(length=512), nullable=True),
                    sa.Column('public_key', sa.Text(), nullable=True),
                    sa.Column('private_key', sa.Text(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('plots')
    # ### end Alembic commands ###