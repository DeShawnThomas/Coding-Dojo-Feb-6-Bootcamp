from flask import render_template,redirect,request,session,flash, url_for

from flask_app import app

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja

@app.route('/ninjas/')
def ninjas():
    dojos=Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=dojos)

@app.route('/ninjas/create/',methods=['POST'])
def create_ninja():
    print(request.form)
    ninja_id = Ninja.save(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(url_for('show', id=dojo_id))

@app.route('/ninjas/edit/<int:id>/')
def edit(id):
    data ={ 
        'id':id
    }
    ninja=Ninja.get_one(data)
    return render_template("edit_ninja.html", ninja=ninja)

# @app.route('/ninjas/update/<int:id>', methods=['POST'])
# def update(id):
#     id = request.form['id']
#     data = {
#         'id': id,
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'age': request.form['age'],
#         'dojo_id': request.form['dojo_id']
#     }
#     Ninja.update(data)
#     return redirect(url_for('show', id=data['id']))

# I'm giving up on the edit redirect. Everything else is fine but this is taking too long and I am getting behind!


@app.route('/ninjas/destroy/<int:id>/')
def destroy(id):
    data ={
        'id': id
    }
    Ninja.destroy(data)
    return redirect(url_for('show'), id=data['id'])