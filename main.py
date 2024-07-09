from chatbot import create_app
from chatbot.spring_data_access import on_open,on_message,on_close,on_error
import websocket
import threading


app,socketio=create_app()

def start_websocket_client():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8080/message",  # Replace with your Spring Boot WebSocket URL
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__=='__main__':

    # Load the secret key from config.py
    app.config.from_pyfile('config.py')

    websocket_thread=threading.Thread(target=start_websocket_client)
    websocket_thread.start()
    #socketio.run(app,debug=True)
    app.run(debug=True,threaded=True)
   
