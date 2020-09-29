from . import db
from datetime import datetime, date


class User(db.Model):
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
    starting_bid = db.Column(db.Integer, nullable = False)
    current_bid = db.Column(db.String(5), nullable = False)
    total_bids = db.Column(db.String(5), nullable = False)
    brand = db.Column(db.String(20), nullable = False)
    cpu = db.Column(db.String(10), nullable = False)
    ram_gb = db.Column(db.Integer, nullable = False)
    storage_gb = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(200), nullable = False)
    condition = db.Column(db.String(10), nullable = False)
    status = db.Column(db.String(10), nullable = False)
    image_url = db.Column(db.String(400), nullable = False)

    # Testing end_date with datetime, will have to change later
    end_date = db.Column(db.DateTime, default = datetime.now())
    seller = db.Column(db.String(80), nullable = False)

    reviews = db.relationship('Review', backref = 'listing')

    def set_review(self, review):
        self.reviews.append(review)

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


class WatchListItem(db.Model):
    __tablename__ = 'watchlistitems'
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default = datetime.now())

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))


