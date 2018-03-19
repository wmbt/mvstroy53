from flask import Blueprint, render_template
from flask_menu import register_menu

mod_heating = Blueprint('heating', __name__, '/')


@register_menu(mod_heating, '.heating', 'Отопление', order=2)
@mod_heating.route('/heating', methods=['GET'])
def index():
    return render_template("heating/index.html")
