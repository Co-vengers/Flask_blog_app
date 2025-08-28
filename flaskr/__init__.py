import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Update the database URI for MySQL
        SQLALCHEMY_DATABASE_URI = 'mysql://root:Vyom2004r@localhost/db2', # Change the values
        SQLALCHEMY_TRACK_MODIFICATIONS=False,  # Disable track modifications to save memory
    )

    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app


