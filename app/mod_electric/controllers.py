from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_electric = Blueprint('electric', __name__, '/')


@register_menu(mod_electric, '.electric', 'Электрика', order=4)
@mod_electric.route('/electric', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.startswith('electric'))
    return render_template("electric/index.html", photos_list=photos_list)
