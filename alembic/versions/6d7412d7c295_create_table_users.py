"""create table users

Revision ID: 6d7412d7c295
Revises: 538755761e27
Create Date: 2020-10-09 11:56:09.814683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d7412d7c295'
down_revision = '538755761e27'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("phone_number", sa.String(), nullable=True),
        sa.Column("organization_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"],),
    )
  op.create_index(op.f("idx_users_email"), "users", ["email"], unique=True)


def downgrade():
  op.drop_index("idx_users_email", table_name="users")
  op.drop_table("users")
