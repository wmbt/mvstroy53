from flask import Blueprint, render_template
from flask_menu import register_menu

mod_watersupply = Blueprint('watersupply', __name__, '/')


@register_menu(mod_watersupply, '.watersupply', 'Водоснабжение', order=3)
@mod_watersupply.route('/watersupply', methods=['GET'])
def index():
    return render_template("watersupply/index.html")
