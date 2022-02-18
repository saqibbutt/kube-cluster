from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Jokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50))
    value = db.Column(db.String(255))

    def __repr__(self):
        return '<Joke %s>' % self.value

class JokesSchema(ma.Schema):
    class Meta:
        fields = ("id", "url", "value")
        model = Jokes

joke_schema = JokesSchema()
jokes_schema = JokesSchema(many=True)

class JokesListResource(Resource):
    def get(self):
        jokes = Jokes.query.all()
        return jokes_schema.dump(jokes)

api.add_resource(JokesListResource, '/jokes')

if __name__ == '__main__':
    app.run()