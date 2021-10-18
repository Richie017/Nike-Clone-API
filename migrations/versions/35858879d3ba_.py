"""empty message

Revision ID: 35858879d3ba
Revises: 82fb05eacad3
Create Date: 2021-10-04 22:02:40.800600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35858879d3ba'
down_revision = '82fb05eacad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='genderenum'), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('country', sa.String(length=30), nullable=True),
    sa.Column('is_notification_enabled', sa.Enum('yes', 'no', name='notificationenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###