"""empty message

Revision ID: dc1747bbc27e
Revises: be09fc2e6de4
Create Date: 2018-09-25 09:32:46.215363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc1747bbc27e'
down_revision = 'be09fc2e6de4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_body'), 'post', ['body'], unique=False)
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.drop_index(op.f('ix_post_body'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
