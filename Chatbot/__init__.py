from flask import Flask
from .routes import routes

def create_app():
    app=Flask(__name__)
    #secret key goes here
    app.register_blueprint(routes,url_prefix='/')
    return app