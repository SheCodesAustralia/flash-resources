from flask import Blueprint, render_template    
from flash.db import get_db

home = Blueprint('home', __name__)


@home.route('/')
def index():
    db = get_db()
    all_projects = db.execute(
        'SELECT name, description FROM projects'
    ).fetchall()
    return render_template('index.html', all_projects=all_projects)


@home.route('/contact')
def contact():
    return render_template('contact.html')
