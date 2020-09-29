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
    print('form is valid')
    return redirect(url_for('listing.createlisting'))
  else:
    print('form is not valid')

  return render_template('listings/createlisting.html', form=form)





