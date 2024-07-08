from chatbot import create_app

app=create_app()

if __name__=='__main__':

    # Load the secret key from config.py
    app.config.from_pyfile('config.py')

    app.run(debug=True)
