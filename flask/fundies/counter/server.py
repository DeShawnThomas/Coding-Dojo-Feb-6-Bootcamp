from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'bing bong'

@app.route('/')
def counter():
    session['count'] = session.get('count', 0) + 1
    return render_template("index.html", count=session['count'])

# @app.route('/plus_two', methods=['POST'])
# def plus_two():
#     value_of_two = int(request.form['two'])
#     session['count'] = session.get('count', 0) + value_of_two
#     return redirect('/')

# originally I had "plus_two" as a route but then I realized I could combine the functionality with an if/elif statement on the request form

@app.route('/count_change', methods=['POST'])
def count_change():
    if 'two' in request.form:
        value_of_two = int(request.form['two'])
        session['count'] = session.get('count', 0) + value_of_two
    elif 'reset' in request.form:
        session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)