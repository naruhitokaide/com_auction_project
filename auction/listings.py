from flask import Blueprint, render_template, request, session, url_for, redirect
from .models import Listing, Review
from auction.forms import ListingForm

# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    listing = get_listing()
    return render_template('listings/showlisting.html', listing=listing)

@listingbp.route('/create', methods=['GET', 'POST'])
def createlisting():
  form = ListingForm()

  if form.validate_on_submit():
    print('form is valid')
    return redirect(url_for('listing.createlisting'))
  else:
    print('form is not valid')

  return render_template('listings/createlisting.html', form=form)

def get_listing():

  # For testing purposes to make sure showlisting.html is updating dynmically 

  listing_description= """ 
    The laptop is in excellent condition with only 61 battery cycles.

    Screen is in like new condition, no scratched marks or dead pixels absolutely perfect.

    Keyboard perfectly functional There is a small chip in the Command Key (see Image) I don't know what has caused it, everything else is perfect condition."""
  
  image_location = 'https://images.unsplash.com/photo-1585247226801-bc613c441316?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80'
  
  listing = Listing('Testing New Lising', '500', listing_description, 'Active', 'Used', image_location, '19/08/2020', 'User1')

  review = Review('User1', 'Great device for school!', 'Awesome computer')
  review2 = Review('User2', 'Amazing!', 'Great so far')

  listing.set_review(review)
  listing.set_review(review2)

  return listing


