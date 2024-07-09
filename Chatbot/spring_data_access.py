def on_message(ws, message):
    print(f"Received message from Spring Boot: {message}")

def on_error(ws,error):
    print(f"Error from Spring Boot WebSocket: {error}")

def on_close(ws,close_status,reason):
    print("Spring Boot WebSocket closed")

def on_open(ws):
    def run():
        ws.send("Hello from Flask-SocketIO")
    run()
