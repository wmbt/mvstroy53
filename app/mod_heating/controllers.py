from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_heating = Blueprint('heating', __name__, '/')


@register_menu(mod_heating, '.heating', 'Отопление', order=2)
@mod_heating.route('/heating', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.startswith('heating'))
    return render_template("heating/index.html", photos_list=photos_list)
