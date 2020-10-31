from flask import Blueprint, render_template, request, session, url_for, redirect, flash, abort
from .models import Listing, Review, Bid, WatchListItem
from auction.forms import ListingForm, ReviewForm, BidForm
from . import db
from werkzeug.utils import secure_filename
import os
from flask_login import login_required, current_user
from datetime import datetime, date


# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    listing = Listing.query.filter_by(id=id).first()
    review_form_instance = ReviewForm()
    bid_form_instance = BidForm()

    return render_template('listings/showlisting.html', listing=listing, form=review_form_instance, bidform=bid_form_instance)

@listingbp.route('/create', methods=['GET', 'POST'])
@login_required #login is required for creating a listing
def createlisting():
  listingform = ListingForm()

  if listingform.validate_on_submit():
    #Check the image file
    db_file_path = check_upload_file(listingform)

    # Write data to database
    listing = Listing()
    
    listing.title = listingform.title.data
    listing.starting_bid = listingform.starting_bid.data
    listing.current_bid = listingform.starting_bid.data
    listing.total_bids = 0
    listing.brand = listingform.brand.data
    listing.cpu =  listingform.cpu.data
    listing.ram_gb = listingform.ram.data
    listing.storage_gb = listingform.storage.data
    listing.condition = listingform.condition.data
    listing.end_date = listingform.end_date.data
    listing.status = 'Active'
    listing.description = listingform.description.data
    listing.image_url = db_file_path
    listing.seller = current_user.name
  
    # Add object to db session
    db.session.add(listing)

    # Commit data to database
    db.session.commit()

    print('form is valid')
    flash("Listing has been posted!", 'success')
    return redirect(url_for('listing.createlisting'))
  else:
    print('form is not valid')

  return render_template('listings/createlisting.html', form=listingform)

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

  # Retrieve count of user listings
  myListingsCount = Listing.query.filter_by(seller=current_user.name).count()

  return render_template('listings/mylistings.html', listings=listings, mylistingscount="({0})".format(myListingsCount))

@listingbp.route('/mylistings/<listing>/close', methods=['GET', 'POST'])
def close_listing(listing):

    # Retrive Listing Object and Bid List
    update_listing = Listing.query.filter_by(id=listing).first()

    # Update status to closed
    update_listing.status = 'Closed' 

    if update_listing.total_bids > 0:
      # Update bid status of higest bid to 'Won'
      highest_bid = Bid.query.filter_by(listing_id=listing, bid_status='Winning').first()
      highest_bid.bid_status = 'Won'
  
    db.session.commit()

    # Re-render page with updated items 
    listings = Listing.query.filter_by(seller=current_user.name).all()
    flash("The listing has been closed", 'success')

    return render_template('listings/mylistings.html', listings=listings)

@listingbp.route('<listing>/watchlist', methods=['GET', 'POST'])
@login_required
def add_watchlist(listing):
    item  = Listing.query.filter_by(id=listing).first()
    watchlist_item = WatchListItem(listing_id = item.id, user_id = current_user.id, date_added=datetime.now())
    
    # Returns true if item is already in the current users watchlist
    itemexists = bool(WatchListItem.query.filter_by(listing_id=item.id, user_id=current_user.id).first())

    if (itemexists):
      flash ("This listing is already in your Watchlist")
    elif (current_user.name == item.seller):
      flash ("Cannot add your own listing to your Watchlist")
    else: 
      flash ("Listing was added to your Watchlist", "success")
      db.session.add(watchlist_item)
      db.session.commit()
    return redirect(url_for('listing.showlisting', id=listing))

@listingbp.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():
    watchListItems = WatchListItem.query.filter_by(user_id = current_user.id).all()
    allListings = Listing.query.filter_by(status='Active').all()
 
    watchlistlistings = []

    # Find listings that are inside of the users watch list
    for watchlistitem in watchListItems:
      for listing in allListings:
        if watchlistitem.listing_id == listing.id:
          watchlistlistings.append(listing)
    
    # Retrieve count of watchlistitems
    watchListCount = WatchListItem.query.filter_by(user_id=current_user.id).count()

    return render_template('listings/watchlist.html', watchlistlistings=watchlistlistings,
     watchlistcount="({0})".format(watchListCount), watchlistitems=watchListItems)


@listingbp.route('/watchlist/<listing>/remove', methods=['GET', 'POST'])
def remove_watchlist(listing):
   update_watchlist = WatchListItem.query.filter_by(listing_id=listing, user_id=current_user.id).first()
   db.session.delete(update_watchlist)
   db.session.commit()

   # Re-render page with updated items 
 
   watchListItems = WatchListItem.query.filter_by(user_id = current_user.id).all()
   allListings = Listing.query.filter_by(status='Active').all()

   watchlistlistings = []

   for watchlistitem in watchListItems:
     for listing in allListings:
       if watchlistitem.listing_id == listing.id:
         watchlistlistings.append(listing)

   # Retrieve count of watchlistitems
   watchListCount = WatchListItem.query.filter_by(user_id=current_user.id).count()

   return render_template('listings/watchlist.html', watchlistlistings=watchlistlistings,
     watchlistcount="({0})".format(watchListCount), watchlistitems=watchListItems)

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

@listingbp.route('/<listing>/bid', methods = ['GET', 'POST'])  
@login_required
def placebid(listing):
    bidform = BidForm()
    listing_obj = Listing.query.filter_by(id=listing).first()

    if bidform.validate_on_submit():  
      # Write to database
      bid = Bid()
      bid.bid_amount = bidform.bid_amount.data
      bid.listing_id = listing_obj.id
      bid.bidder_name = current_user.name

      # Check that user is not bidding on their own listing
      if listing_obj.seller != current_user.name:

        # Check if bid is more than current bid 
        if bid.bid_amount > listing_obj.current_bid:
          listing_obj.current_bid = bid.bid_amount

          # Set bid status to winning
          bid.bid_status = 'Winning'

          # Add bid to db
          db.session.add(bid)

          # Set bid status of all other bids to 'Outbid'
          oldbids = Bid.query.filter_by(listing_id = listing).all()
          for bid in oldbids[:-1]:
            bid.bid_status = 'Outbid'

          # Update total bids 
          update_total_bids = Listing.query.filter_by(id=listing).first()
          update_total_bids.total_bids += 1

          # Commit bid to db
          db.session.commit()
          
          flash("Bid was successfully placed!", 'success')
          print('Bid was successfully placed!')
        else: 
          flash ("Bid amount has to be higher than current bid")
      else:
        flash("You cannot bid on your own listing", 'danger')
        print('User cannot bid on their own listing')
         
    else: 
      print('Bid form is not valid')
    return redirect(url_for('listing.showlisting', id=listing))
