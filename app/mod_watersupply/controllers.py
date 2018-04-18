from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_watersupply = Blueprint('watersupply', __name__, '/')


@register_menu(mod_watersupply, '.watersupply', 'Водоснабжение', order=3)
@mod_watersupply.route('/watersupply', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.startswith('watersupply'))
    return render_template("watersupply/index.html", photos_list=photos_list)
