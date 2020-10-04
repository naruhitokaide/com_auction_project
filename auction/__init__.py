from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os 

db = SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)

    # Set app configuration data
    os.environ['DATABASE_URL'] = 'sqlite:///auction.sqlite'
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///auction.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
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

    #initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view='authentication.login'
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app