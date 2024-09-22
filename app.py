from flask import Flask
from urls import blue_print

def create_app():
    app = Flask(__name__)

    app.register_blueprint(blue_print)

    return app

app = create_app()

app.run()