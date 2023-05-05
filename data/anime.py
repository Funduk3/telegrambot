import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Anime(SqlAlchemyBase):
    __tablename__ = 'anime'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    titles = sqlalchemy.Column(nullable=True)
