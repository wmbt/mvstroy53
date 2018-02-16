from flask import Flask
from app.mod_home.controllers import mod_home


app = Flask(__name__)

app.config.from_object('config')

app.register_blueprint(mod_home)
