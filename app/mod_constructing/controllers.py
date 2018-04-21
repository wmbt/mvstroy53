from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_constructing = Blueprint('constructing', __name__, '/')


@register_menu(mod_constructing, '.constructing', 'Строительство', order=6)
@mod_constructing.route('/constructing', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.startswith('ventilation'))
    return render_template("constructing/index.html", photos_list=photos_list)
