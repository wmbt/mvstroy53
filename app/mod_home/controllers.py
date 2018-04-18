from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_home = Blueprint('home', __name__, '/')


@register_menu(mod_home, '.home', 'Главная', order=1)
@mod_home.route('/', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.endswith('f.jpg'))
    return render_template("home/index.html", photos_list=photos_list)
