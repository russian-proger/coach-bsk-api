import datetime
import os

import flask
import sqlalchemy.orm as orm
import sqlalchemy as sqla

env = os.environ

mysql_uri = f"mysql://{env['MYSQL_USER']}:{env['MYSQL_PASSWORD']}@{env['MYSQL_HOST']}:{env['MYSQL_PORT']}/{env['MYSQL_DB']}?charset=utf8mb4"

engine = sqla.create_engine(mysql_uri)

class Base(orm.DeclarativeBase):
    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

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

Base.metadata.create_all(bind=engine)

app = flask.Flask(__name__)
app.secret_key = "1234"

@app.get('/books')
def get_books():
    with orm.Session(engine) as session:
        res = session.query(Book).all()
        return flask.jsonify([i.serialize() for i in res])
    
@app.post('/book')
def post_book():
    json = flask.request.get_json()

    with orm.Session(engine) as session:
        book = Book()
        book.gym = json.get('gym', '')
        book.coach = json.get('coach', '')
        book.train_type = json.get('train_type', '')
        book.train_kind = json.get('train_kind', '')

        if 'date' in json:
            book.date = json['date']

        session.add(book)
        session.commit()
        return "OK", 201

@app.get('/tournaments')
def get_tournaments():
    with orm.Session(engine) as session:
        res = session.query(Tournament).all()
        return flask.jsonify([i.serialize() for i in res])
    
@app.post('/tournament')
def post_tournament():
    json = flask.request.get_json()

    with orm.Session(engine) as session:
        tournament = Tournament()
        tournament.name = json.get('name', '')
        tournament.team_1 = json.get('team_1', '')
        tournament.team_2 = json.get('team_2', '')
        tournament.players = json.get('players', '')

        if 'date' in json:
            tournament.date = json['date']

        session.add(tournament)
        session.commit()
        return "OK", 201

if __name__ == "__main__":
    app.run(env['HTTP_HOST'], env['HTTP_PORT'])