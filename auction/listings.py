from flask import Blueprint, render_template
from .models import Listing, Review

# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    listing = get_listing()
    return render_template('listings/showlisting.html', listing=listing)


def get_listing():

  # For testing purposes to make sure showlisting.html is updating dynmically 


  listing_description= """ 
    The laptop is in excellent condition with only 61 battery cycles.

    Screen is in like new condition, no scratched marks or dead pixels absolutely perfect.

    Keyboard perfectly functional There is a small chip in the Command Key (see Image) I don't know what has caused it, everything else is perfect condition."""
  
  image_location = 'https://images.unsplash.com/photo-1585247226801-bc613c441316?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80'
  
  listing = Listing('Testing New Lising', '500', '899', 18, listing_description, 'Active', 'Used', image_location, '12:01:56', 'User1')
  
  # test reviews
  review = Review('User1', 'Great device for school!', 'Awesome computer')
  review2 = Review('User2', 'Amazing!', 'Great so far')

  listing.set_review(review)
  listing.set_review(review2)

  return listing