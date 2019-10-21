"""followers

Revision ID: 67be9de54353
Revises: 6b18cc72f55c
Create Date: 2019-10-06 22:22:22.344170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67be9de54353'
down_revision = '6b18cc72f55c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
