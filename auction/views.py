from flask import Blueprint, render_template, request, redirect, url_for, flash 
from .models import Listing
from sqlalchemy import or_

# Create main blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    listings = Listing.query.filter_by(status='Active').all()
    return render_template('index.html', listings=listings)

@mainbp.route('/search')
def search():
    #get the search string from request
    if request.args['search']:
        item = "%" + request.args['search'] + '%'
    #use filter and like function to search for matching item
        listing = Listing.query.filter(
            or_(
                Listing.title.like(item),
                Listing.cpu.like(item),
                Listing.brand.like(item),
                Listing.ram_gb.like(item),
                Listing.storage_gb.like(item)
            ), Listing.status=='Active'
        )
        # Search result message 
        resultMessage = "{0} results matching '{1}'".format(listing.count(), request.args['search'])
        flash (resultMessage)
        return render_template('index.html', listings=listing)
    else:
        return redirect(url_for('main.index'))