from flask import Blueprint, session, redirect, url_for, render_template, flash
from auction.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash

authenticationbp = Blueprint('authentication', __name__, url_prefix='/authentication')

@authenticationbp.route('/login', methods=['GET', 'POST'])
def login():
    login_form_instance = LoginForm();

    if login_form_instance.validate_on_submit():
        session['email'] = login_form_instance.user_name.data
        return redirect(url_for('authentication.login'))

    return render_template('authentication/login.html', form=login_form_instance)

@authenticationbp.route('/register', methods=['GET', 'POST'])
def register():
    register_form_instance = RegisterForm();

    if register_form_instance.validate_on_submit():
        return redirect(url_for('authentication.register'))

    return render_template('authentication/register.html', form=register_form_instance)

@authenticationbp.route('/logout')
def logout():
    session.clear()
    return render_template('authentication/logout.html')