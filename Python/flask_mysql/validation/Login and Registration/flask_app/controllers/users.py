from flask import render_template,request,session,redirect, flash
from flask_app import app

from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    
    user_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confirm_password": request.form['confirm_password'],
    }

    hashed_password = bcrypt.generate_password_hash(user_data['password'])
    user_data['password'] = hashed_password

    user_id = User.save(user_data)
    
    session['user_id'] = user_id
    
    return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login_user():
    user = User.get_one_by_email(request.form['email'])

    if not User.validate_login(request.form):
        return redirect('/') 

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/welcome')


@app.route('/welcome')
def welcome():

    if 'user_id' not in session:
        return redirect('/logout')

    user=User.get_one(session['user_id'])
    
    return render_template('logout.html', user=user)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
