from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_restful import Api


from back.common.db import Db
from back.models.users.user import User
from back.models.users.views import Login, Test

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app.config['JWT_SECRET_KEY'] = 'caiaffa'
app.config['JWT_BLACKLIST_ENABLED'] = True
jwt = JWTManager(app)


api.add_resource(Login, '/login/')
api.add_resource(Test, '/test/')
app.register_blueprint(api_bp)


@app.route('/')
def hello_word():
    user = User.find_email('lfa.luisfelipe@gmail.com')
    return 'Hello word'


@app.before_first_request
def initialize_database():
    Db.initialize()
