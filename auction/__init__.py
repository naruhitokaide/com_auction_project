from flask import Flask

def create_app():
    print(__name__)
    app = Flask(__name__)

    from . import views
    app.register_blueprint(views.mainbp)
    
    return app