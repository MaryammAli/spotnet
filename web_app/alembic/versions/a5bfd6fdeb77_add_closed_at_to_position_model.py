"""Add closed_at to Position model

Revision ID: a5bfd6fdeb77
Revises: 628064f52eb0
Create Date: 2025-01-08 22:52:10.951157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5bfd6fdeb77'
down_revision = '628064f52eb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add closed_at to Position model"""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('closed_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Remove closed_at from Position model"""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('position', 'closed_at')
    # ### end Alembic commands ###
