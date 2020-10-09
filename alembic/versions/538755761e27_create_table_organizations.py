"""create table organizations

Revision ID: 538755761e27
Revises: 
Create Date: 2020-10-09 11:30:40.155436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "538755761e27"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
        "organizations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("phone_number", sa.String(), nullable=True),
    )
  op.create_index(op.f("idx_organizations_email"), "organizations", ["email"], unique=True)

def downgrade():
  op.drop_index("idx_organizations_email", table_name="organizations")
  op.drop_table("organizations")
