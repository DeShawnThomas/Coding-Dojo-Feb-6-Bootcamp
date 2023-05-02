from flask import render_template,redirect,request,session,flash, url_for

from flask_app import app

from flask_app.models.usercrud import User

@app.route('/')
def index():
    return redirect('/users/')

@app.route('/users/')
def users():
    users=User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/users/new/')
def new():
    return render_template("newuser.html")

@app.route('/users/create/',methods=['POST'])
def create():
    print(request.form)
    user_id = User.save(request.form)
    return redirect(url_for('show', id=user_id))

# Users CRUD new ones... oh I was wondering wtf a "CR" was and I see now ha!) I am really hoping I didnt modularize this early... I figured that was the standard....

@app.route('/users/<int:id>')
def show(id):
    data = {
        'id': id
        }
    one_user = User.get_one(data)
    return render_template("createduser.html", user=one_user)

@app.route('/users/edit/<int:id>/')
def edit(id):
    data ={ 
        'id':id
    }
    user=User.get_one(data)
    return render_template("edituser.html", user=user)

@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>/')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')