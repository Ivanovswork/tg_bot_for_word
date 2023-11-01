import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_file import FileField


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = sq.Column(sq.Integer, autoincrement=True, primary_key=True)
    tg_id = sq.Column(sq.Integer, unique=True)


class Text(Base):
    __tablename__ = "text"

    id = sq.Column(sq.Integer, autoincrement=True, primary_key=True)
    text_file = sq.Column(FileField, unique=True)

    user_id = sq.Column(sq.Integer, sq.ForeignKey('user.id', ondelete='CASCADE'), nullable=False,)

