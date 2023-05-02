from flask import render_template,redirect,request,session,flash, url_for

from flask_app import app

from flask_app.models.dojo import Dojo 

from flask_app.models.ninja import Ninja 

# redirects home page to "/dojos"
@app.route('/')
def index():
    return redirect('/dojos/')

@app.route('/dojos/')
def dojos():
    dojos=Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route('/dojos/create/',methods=['POST'])
def create():
    print(request.form)
    dojo_id = Dojo.save(request.form)
    return redirect('/dojos/')

@app.route('/dojos/<int:id>')
def show(id):
    data = {
        'id': id
    }
    dojos = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojo_location.html", one_dojo=dojos)