"""Initial migration.

Revision ID: 2bbac961f431
Revises: 22bc01988e55
Create Date: 2024-05-24 11:24:40.055818

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "2bbac961f431"
down_revision = "22bc01988e55"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("description", sa.String(length=256), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("task")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task",
        sa.Column("id", mysql.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", mysql.VARCHAR(length=128), nullable=False),
        sa.Column("description", mysql.VARCHAR(length=256), nullable=True),
        sa.Column("created_at", mysql.DATETIME(), nullable=True),
        sa.Column("updated_at", mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_0900_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.drop_table("tasks")
    # ### end Alembic commands ###
