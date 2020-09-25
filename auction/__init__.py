from flask import Flask
from . import views, listings, auth
from flask_bootstrap import Bootstrap

def create_app():
    print(__name__)
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(views.mainbp)
    app.register_blueprint(listings.listingbp)
    app.register_blueprint(auth.authenticationbp)

    # Initialise bootstrap 
    bootstrap = Bootstrap(app)

    return app