from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from src import db
from datetime import date

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(100), index=True, unique=True)
    date: so.Mapped[date] = so.mapped_column(sa.Date)

    def __repr__(self):
        return "<Post {}>".format(self.title)
