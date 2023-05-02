from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", columns=8, rows=8)

# @app.route('/<int:4>')
# def half_board():
#     return render_template("index.html", columns=8, rows=4)

# @app.route('/<int:columns>/<int:rows>')
# def custom_board(columns, rows):
#     return render_template("index.html", columns= columns, rows= rows)


if __name__=="__main__":
    app.run(debug=True)