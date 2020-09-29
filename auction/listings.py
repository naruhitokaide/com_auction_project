from flask import Blueprint, render_template, request, session, url_for, redirect
from .models import Listing, Review
from auction.forms import ListingForm, ReviewForm
from . import db

# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    listing = Listing.query.filter_by(id=id).first()
    review_form_instance = ReviewForm()
    return render_template('listings/showlisting.html', listing=listing, form=review_form_instance)

@listingbp.route('/create', methods=['GET', 'POST'])
def createlisting():
  form = ListingForm()

  if form.validate_on_submit():
    # Write data to database
    listing = Listing()
    
    listing.title = form.title.data
    listing.starting_bid = form.starting_bid.data
    listing.current_bid = form.starting_bid.data
    listing.total_bids = 0
    listing.brand = form.brand.data
    listing.cpu =  form.cpu.data
    listing.ram_gb = form.ram.data
    listing.storage_gb = form.storage.data
    listing.condition = form.condition.data
    listing.end_date = form.end_date.data
    listing.status = 'Active'
    listing.description = form.description.data
    listing.image_url = form.image.data

    # Add object to db session
    db.session.add(listing)

    # Commit data to database
    db.session.commit() 

    print('form is valid')
    return redirect(url_for('listing.createlisting'))
  else:
    print('form is not valid')

  return render_template('listings/createlisting.html', form=form)





