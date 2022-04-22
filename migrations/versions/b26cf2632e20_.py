"""empty message

Revision ID: b26cf2632e20
Revises: a174b592e488
Create Date: 2022-04-23 02:08:24.996605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26cf2632e20'
down_revision = 'a174b592e488'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('video_tags_video_id_key', 'video_tags', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('video_tags_video_id_key', 'video_tags', ['video_id'])
    # ### end Alembic commands ###