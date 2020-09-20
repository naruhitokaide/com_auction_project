from flask import Blueprint, render_template

# Create main blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')