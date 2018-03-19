from flask import Blueprint, render_template
from flask_menu import register_menu

mod_home = Blueprint('home', __name__, '/')


@register_menu(mod_home, '.home', 'Главная', order=1)
@mod_home.route('/', methods=['GET'])
def index():
    return render_template("home/index.html")
