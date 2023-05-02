from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'orange juice jones'

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    session['name'] = name
    session['location'] = location
    session['language'] = language
    session['comments'] = comments

    return redirect("/result")

@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    language = session.get('language')
    comments = session.get('comments')

    return render_template('result.html', name=name, location=location, language=language, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)