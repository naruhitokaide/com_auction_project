from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)

    # Set app configuration data
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///auction.sqlite'
    db.init_app(app)
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Import blueprints and models
    from auction.views import mainbp
    from auction.listings import listingbp
    from auction.auth import authenticationbp
    from auction.models import User

    # Register blueprints
    app.register_blueprint(mainbp)
    app.register_blueprint(listingbp)
    app.register_blueprint(authenticationbp)

    # Initialise bootstrap 
    bootstrap = Bootstrap(app)

    return app