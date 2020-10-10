from flask import Blueprint, render_template, request, session, url_for, redirect
from .models import Listing, Review
from auction.forms import ListingForm, ReviewForm
from . import db
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, current_user


# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    listing = Listing.query.filter_by(id=id).first()
    review_form_instance = ReviewForm()
    return render_template('listings/showlisting.html', listing=listing, form=review_form_instance)


@listingbp.route('/create', methods=['GET', 'POST'])
@login_required #login is required for creating a listing
def createlisting():
  form = ListingForm()

  if form.validate_on_submit():
    #Check the image file
    db_file_path = check_upload_file(form)

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
    listing.image_url = db_file_path
    listing.seller = current_user.name
  
    # Add object to db session
    db.session.add(listing)

    # Commit data to database
    db.session.commit()

    print('form is valid')
    return redirect(url_for('listing.createlisting'))
  else:
    print('form is not valid')

  return render_template('listings/createlisting.html', form=form)

def check_upload_file(form):
  fp = form.image_url.data
  filename = fp.filename
  BASE_PATH = os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  db_upload_path = '/static/img/'+ secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path


@listingbp.route('/mylistings', methods=['GET', 'POST'])
@login_required
def mylistings():
  listings = Listing.query.filter_by(seller=current_user.name).all()
  return render_template('listings/mylistings.html', listings=listings)


@listingbp.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():
  return render_template('listings/watchlist.html')


@listingbp.route('/<listing>/review', methods = ['GET', 'POST'])  
@login_required
def review(listing):
    form = ReviewForm()
    listing_obj = Listing.query.filter_by(id=listing).first()

    if form.validate_on_submit():  
      review = Review(title=form.title.data, feedback=form.feedback.data,  
                        listing=listing_obj.id, user=current_user)
      db.session.add(review)
      db.session.commit()
      print('Thank you for submitting a review of this item', 'success') 
    return redirect(url_for('listing.showlisting', id=listing))