from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground_one():
    return render_template("index1.html")

@app.route('/play/<int:x>')
def playground_two(x):
    return render_template("index2.html", times = int(x))

@app.route('/play/<int:x>/<string:color>')
def playground_three(x, color):
    return render_template("index3.html", times = int(x), hue = color)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)