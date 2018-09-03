from flask import Flask
from flask_restful import Api
from flask_jwt import JWT # JWT stands for JSON Web Token
from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import StoreList, Store
app = Flask(__name__)
app.secret_key = 'MY_SECRET_KEY :p'   # a secret key must be specified
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
api = Api(app)


jwt = JWT(app, authenticate, identify) # it creates an endpoint called /auth

# adding Resource to API
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


# if this program is the main program (i.e. it is not an import to another python file), the following code below the condition would execute
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True) # debug: for a clear html error msgs
