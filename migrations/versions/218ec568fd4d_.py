"""empty message

Revision ID: 218ec568fd4d
Revises: 7e82119582c3
Create Date: 2022-04-22 18:42:39.259576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218ec568fd4d'
down_revision = '7e82119582c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_duration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.String(length=255), nullable=True),
    sa.Column('video_duration', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['video_id'], ['yt_videos.video_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('video_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_duration')
    # ### end Alembic commands ###
