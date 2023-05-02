from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_app.controllers import recipes

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('new_recipe.html')

@app.route('/recipes/new/create', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/login')
    
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')


    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_thirty': request.form['under_thirty'],
    }

    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('view_recipe.html',recipe=Recipe.get_one_by_id({'id': id}))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('edit_recipe.html',recipe=Recipe.get_one_by_id({'id': id}))

@app.route('/recipes/edit/change/<int:id>', methods=['POST'])
def edit_recipe_change(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')

    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_thirty': request.form['under_thirty'],
    }
    
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/login')

    Recipe.delete({'id':id})
    return redirect('/dashboard')