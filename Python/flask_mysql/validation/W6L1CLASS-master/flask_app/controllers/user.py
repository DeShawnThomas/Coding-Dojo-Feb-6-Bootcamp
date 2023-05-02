from flask import render_template,request,session,redirect
from flask_app import app

from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    # print(request.form['action'])
    if request.form['action'] == 'register':

        is_valid = user.User.validate_user(request.form)
        if not is_valid:
            return redirect("/")
        #w6l1
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data={
            'first_name': request.form['f_name'].strip().lower(),
            'last_name':request.form['l_name'].strip().lower(),
            'email':request.form['email'].strip().lower(),
            'password':pw_hash
        }

        id = user.User.save(data)
        print(f"THIS IS THE ID: {id}")
        
        session['user_id'] = id

        return redirect("/dash")
    else:
        is_valid = user.User.validate_user(request.form)
        if not is_valid:
            return redirect("/")
        
        this_user = user.User.get_one_by_email(request.form['email'])
        if not this_user:
            return redirect("/")
        if this_user.password == request.form['password']:
            session['user_id']=this_user.id
            return redirect("/dash")
        else:
            return redirect("/")

@app.route("/dash")
def dash():
    if 'user_id' not in session:
        return redirect("/")

    users = user.User.get_all()
    return render_template("dash.html",users=users)

@app.route("/users/<int:id>/edit")

def edit_view(id):
    if 'user_id' not in session:
        return redirect("/")
    return render_template("update.html",user=user.User.get_one(id))

@app.route("/users/<int:id>/update",methods=["POST"])
def update_user(id):
    if 'user_id' not in session:
        return redirect("/")
    if not session['user_id'] == id:
        return redirect("/")
    data={
        'first_name':request.form['f_name'],
        'last_name':request.form['l_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'id':id
    }
    user.User.update(data)
    return redirect("/dash")

@app.route("/users/<int:id>/destroy")
def delete(id):
    if 'user_id' not in session:
        return redirect("/")
    if not session['user_id'] == id:
        return redirect("/")    
    user.User.delete(id)
    return redirect("/dash")

@app.route("/logout")
def logout():
    session.clear() 
    return redirect("/")