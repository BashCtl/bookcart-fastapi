"""update books table

Revision ID: 6494b76cd907
Revises: 7a685fd42b04
Create Date: 2024-01-30 11:28:17.052301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6494b76cd907'
down_revision: Union[str, None] = '7a685fd42b04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_book_title_uc', 'books', ['title', 'author_id', 'category_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_book_title_uc', 'books', type_='unique')
    # ### end Alembic commands ###