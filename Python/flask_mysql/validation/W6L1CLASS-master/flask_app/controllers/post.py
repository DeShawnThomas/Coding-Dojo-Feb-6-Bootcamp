from flask import render_template,request,session,redirect
from flask_app import app

from flask_app.models import post

# from flask_app.models.user import User

@app.route("/posts/new")
def new_post():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("new_post.html")

@app.route("/posts/create",methods=["POST"])
def create_post():
    if 'user_id' not in session:
        return redirect("/")
    data={
        'img_url':request.form['img_url'],
        'comment':request.form['comment'],
        'user_id':session['user_id']
    }
    post.Post.save(data)
    return redirect("/posts")



@app.route("/posts")
def post_dash():
    if 'user_id' not in session:
        return redirect("/")
    posts = post.Post.get_all()
    return render_template("posts.html",posts=posts)

@app.route("/users/<int:id>/posts")
def user_post_dash(id):
    if 'user_id' not in session:
        return redirect("/")
    posts = post.Post.get_all()
    return render_template("user_post.html",posts=posts,id=id)

@app.route("/posts/<int:id>/edit")

def post_edit_view(id):
    if 'user_id' not in session:
        return redirect("/")
    return render_template("update_post.html",post=post.Post.get_one(id))

@app.route("/posts/<int:id>/update",methods=["POST"])
def update_post(id):
    if 'user_id' not in session:
        return redirect("/")
    data={
        'img_url':request.form['img_url'],
        'comment':request.form['comment'],
        'user_id':session['user_id'],
        'id':id
    }
    post.Post.update(data)
    return redirect("/posts")

@app.route("/posts/<int:id>/destroy")
def post_delete(id):
    if 'user_id' not in session:
        return redirect("/")
    post.Post.delete(id)
    return redirect("/posts")

@app.route("/posts/<int:id>/like")
def post_like(id):
    if 'user_id' not in session:
        return redirect("/")
    post.Post.like(id,session['user_id'])
    return redirect("/posts")