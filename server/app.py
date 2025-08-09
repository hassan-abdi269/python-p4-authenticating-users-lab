from flask import Flask
from flask_restful import Api
from config import db, migrate
from models import User, Article
from resources.sessions import Login, Logout, CheckSession

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "dev-secret"

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
