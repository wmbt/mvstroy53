from flask import Blueprint, render_template
from flask_menu import register_menu

from app.common.photos import get_photos_list

mod_ventilation = Blueprint('ventilation', __name__, '/')


@register_menu(mod_ventilation, '.ventilation', 'Вентиляция', order=5)
@mod_ventilation.route('/ventilation', methods=['GET'])
def index():
    photos_list = get_photos_list(lambda x: x.startswith('ventilation'))
    return render_template("ventilation/index.html", photos_list=photos_list)
