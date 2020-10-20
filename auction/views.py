from flask import Blueprint, render_template, request, redirect, url_for
from .models import Listing

# Create main blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    listings = Listing.query.all()
    return render_template('index.html', listings=listings)

@mainbp.route('/search')
def search():
    #get the search string from request
    if request.args['search']:
        item = "%" + request.args['search'] + '%'
    #use filter and like function to search for matching item
        listing = Listing.query.filter(Listing.title.like(item)).all()
        return render_template('index.html', listings=listing)
    else:
        return redirect(url_for('main.index'))