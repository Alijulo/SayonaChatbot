from flask import Flask
from .routes import routes
from flask_socketio import SocketIO
from flask_cors import CORS

socketio=SocketIO()
def create_app():
    app=Flask(__name__)
    CORS(app) # Enable CORS for all routes,
    #secret key goes here
    app.register_blueprint(routes,url_prefix='/')
   # Initialize SocketIO
    socketio.init_app(app)
    return app,socketio