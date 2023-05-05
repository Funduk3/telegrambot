import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Series(SqlAlchemyBase):
    __tablename__ = 'series'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    titles = sqlalchemy.Column(sqlalchemy.String, nullable=True)
