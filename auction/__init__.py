from flask import Flask
from . import views, listings

def create_app():
    print(__name__)
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(views.mainbp)
    app.register_blueprint(listings.listingbp)


    return app