import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # set up connection to database
    app.config.from_mapping(
        DATABASE=os.path.join(
            app.instance_path,
            'projects.sqlite'
        ),
    )

    # makes sure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register the home blueprint
    from .home import home
    app.register_blueprint(home)

    from . import db
    db.init_app(app)
    
    return app
