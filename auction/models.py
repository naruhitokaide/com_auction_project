class Listing: 
    def __init__(self, title, starting_bid, current_bid, total_bids, description, status, condition, image, time_left, seller):
        self.title = title
        self.starting_bid = starting_bid
        self.current_bid = current_bid
        self.total_bids = total_bids
        self.description = description
        self.condition = condition
        self.status = status
        self.image = image
        self.time_left = time_left
        self.seller = seller
        self.reviews = list()

    def set_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        debug_string = 'Title: {}, Start Bid: {}, Current Bid: {}, Total Bids: {}, Description: {}, Condition: {}, Time Left {}, Seller: {}'
        debug_string.format(self.title, self.starting_bid, self.current_bid, self.total_bids, self.description, self.condition, self.time_left, self.seller)
        return debug_string


class Review: 
    def __init__ (self, user, title, feedback):
        self.user = user
        self.title = title
        self.feedback = feedback

    def __repr__(self):
        debug_string = 'User: {}, Title: {}, Feedback: {}'
        debug_string.format(self.user, self.title, self.feedback)
        return debug_string

