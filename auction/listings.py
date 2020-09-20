from flask import Blueprint, render_template

# Create listing blueprint
listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/<id>')
def showlisting(id):
    return render_template('listings/showlisting.html')