from flask import Blueprint, render_template
from .models import Listing

# Create main blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    listings = Listing.query.all()
    return render_template('index.html', listings=listings)
