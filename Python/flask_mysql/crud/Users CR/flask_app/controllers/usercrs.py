from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.usercr import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users=User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/users/new')
def new():
    return render_template("newuser.html")

@app.route('/users/create',methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')
