from flask import Blueprint, render_template
from flask_menu import register_menu

mod_electric = Blueprint('electric', __name__, '/')


@register_menu(mod_electric, '.electric', 'Электрика', order=4)
@mod_electric.route('/electric', methods=['GET'])
def index():
    return render_template("electric/index.html")
