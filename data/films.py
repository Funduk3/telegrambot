import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Films(SqlAlchemyBase):
    __tablename__ = 'films'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    titles = sqlalchemy.Column(sqlalchemy.String, nullable=True)
