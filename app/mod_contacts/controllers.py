from flask import Blueprint, render_template
from flask_menu import register_menu

mod_contacts = Blueprint('contacts', __name__, '/')


@register_menu(mod_contacts, '.contacts', 'Контакты', order=7)
@mod_contacts.route('/contacts', methods=['GET'])
def index():
    return render_template("contacts/index.html")
