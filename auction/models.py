from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    reviews = db.relationship('Review', backref = 'user')

# TODO 
# The rest of these below will have to be changed to use SQLAlchemy
# Delete 'auction.sqlite' and rerun 'create_database.py' once classes are setup

class Listing(db.Model): 
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    starting_bid = db.Column(db.Integer(5), nullable = False)
    current_bid = db.Column(db.String(5), nullable = False)
    total_bids = db.Column(db.String(5), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    condition = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(10), nullable = False)
    image = db.Column(db.String(400), nullable = False)
    time_left = db.Column(db.Integer(20), nullable = False)
    seller = db.Column(db.String(80), nullable = False)

    reviews = db.relationship('Review', backref = 'listing')

    # def __init__(self, title, starting_bid, description, status, condition, image, end_date, seller):
    #     self.title = title
    #     self.starting_bid = starting_bid
    #     self.current_bid = starting_bid
    #     self.total_bids = 0
    #     self.description = description
    #     self.condition = condition
    #     self.status = status
    #     self.image = image
    #     self.end_date = end_date
    #     self.seller = seller
    #     self.reviews = list()

    def set_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        debug_string = 'Title: {}, Start Bid: {}, Current Bid: {}, Total Bids: {}, Description: {}, Condition: {}, Time Left {}, Seller: {}'
        debug_string.format(self.title, self.starting_bid, self.current_bid, self.total_bids, self.description, self.condition, self.time_left, self.seller)
        return debug_string

class Review(db.Model):
    __tablename__ = 'reviews' 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    feedback = db.Column(db.String(400), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now())

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __repr__(self):
        debug_string = 'User: {}, Title: {}, Feedback: {}'
        debug_string.format(self.user, self.title, self.feedback)
        return debug_string
    

    # def __init__ (self, user, title, feedback):
    #     self.user = user
    #     self.title = title
    #     self.feedback = feedback

    



