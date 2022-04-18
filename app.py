import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wiyrhyyewrjdhy:400ecfec31042b6b9e3d0a0d84731be0f54cc70f3d4417f26fd055bda6b4fe1f@ec2-52-73-155-171.compute-1.amazonaws.com:5432/dot5mal3v909b"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'some secret key'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)