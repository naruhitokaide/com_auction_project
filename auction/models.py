from . import db
from datetime import datetime, date
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email_id = db.Column(db.String(100), index=True, nullable=False)
    contact_num = db.Column(db.String(15), index=True, nullable=False)
    address = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', backref = 'user')

class Listing(db.Model): 
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    starting_bid = db.Column(db.Float, nullable = False)
    current_bid = db.Column(db.Float, nullable = False)
    total_bids = db.Column(db.Integer, nullable = False)
    brand = db.Column(db.String(20), nullable = False)
    cpu = db.Column(db.String(10), nullable = False)
    ram_gb = db.Column(db.String(10), nullable = False)
    storage_gb = db.Column(db.String(10), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    condition = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(10), nullable = False)
    image_url = db.Column(db.String(400), nullable = False)
    end_date = db.Column(db.DateTime, nullable = False)
    seller = db.Column(db.String(15), nullable = False)

    # Relationship to call listing.reviews
    reviews = db.relationship('Review', backref='listingreviews') 
    # Relationship to call listing.bids
    bids = db.relationship('Bid', backref='listingbids') 

    def set_review(self, review):
        self.reviews.append(review)

class Review(db.Model):
    __tablename__ = 'reviews' 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    feedback = db.Column(db.String(400), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now())

    #Foreign Keys
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __repr__(self):
        debug_string = 'User: {}, Title: {}, Feedback: {}'
        debug_string.format(self.user, self.title, self.feedback)
        return debug_string

class WatchListItem(db.Model):
    __tablename__ = 'watchlistitems'
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default = datetime.now())

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.Float, nullable = False)
    bid_date = db.Column(db.DateTime, default = datetime.now())
    bid_status = db.Column(db.String(80), nullable = False)

    # Foreign Keys 
    bidder_name = db.Column(db.String(100), db.ForeignKey('users.name'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
