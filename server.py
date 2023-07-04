import os

from flask import Flask
import sqlalchemy.orm as orm
import sqlalchemy as sqla

env = os.environ

mysql_uri = f"mysql://{env['MYSQL_USER']}:{env['MYSQL_PASSWORD']}@{env['MYSQL_HOST']}:{env['MYSQL_PORT']}/{env['MYSQL_DB']}?charset=utf8mb4"

engine = sqla.create_engine(mysql_uri)

class Base(orm.DeclarativeBase): pass

class Book(Base):
    __tablename__ = "book"

    id         = sqla.Column(sqla.Integer, primary_key=True, index=True)
    gym        = sqla.Column(sqla.String(256))
    coach      = sqla.Column(sqla.String(256))
    train_type = sqla.Column(sqla.String(256))
    train_kind = sqla.Column(sqla.String(256))
    date       = sqla.Column(sqla.DateTime)

class Tournament(Base):
    __tablename__ = "tournament"

    id         = sqla.Column(sqla.Integer, primary_key=True, index=True)
    name       = sqla.Column(sqla.String(256))
    team_1     = sqla.Column(sqla.String(256))
    team_2     = sqla.Column(sqla.String(256))
    players    = sqla.Column(sqla.String(256))
    date       = sqla.Column(sqla.DateTime)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = Flask(__name__)
app.secret_key = "1234"
