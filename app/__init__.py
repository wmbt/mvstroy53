from flask import Flask
from flask_menu import Menu

from app.mod_home.controllers import mod_home
from app.mod_heating.controllers import mod_heating
from app.mod_watersupply.controllers import mod_watersupply
from app.mod_electric.controllers import mod_electric
from app.mod_ventilation.controllers import mod_ventilation
from app.mod_contacts.controllers import mod_contacts


app = Flask(__name__)
Menu(app=app)

app.config.from_object('config')

app.register_blueprint(mod_home)
app.register_blueprint(mod_heating)
app.register_blueprint(mod_watersupply)
app.register_blueprint(mod_electric)
app.register_blueprint(mod_ventilation)
app.register_blueprint(mod_contacts)
