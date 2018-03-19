from flask import Blueprint, render_template
from flask_menu import register_menu

mod_ventilation = Blueprint('ventilation', __name__, '/')


@register_menu(mod_ventilation, '.ventilation', 'Вентиляция', order=5)
@mod_ventilation.route('/ventilation', methods=['GET'])
def index():
    return render_template("ventilation/index.html")
