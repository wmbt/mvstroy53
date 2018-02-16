from flask import Blueprint, render_template

mod_home = Blueprint('home', __name__, '/')


@mod_home.route('/', methods=['GET'])
def index():
    return render_template("home/maintenance.html")
