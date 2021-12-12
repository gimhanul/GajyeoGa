from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

from app.main.controller import main as main

app.register_blueprint(main)