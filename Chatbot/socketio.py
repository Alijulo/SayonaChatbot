from flask_socketio import emit
from .import socketio


@socketio.on('message',namespace='/socket.io/message') #/socket.io/message
def handle_message(message):
    print('Received message:', message)
    # Process message and send response if needed
    emit('response', {'data': 'Message received'}, broadcast=True)