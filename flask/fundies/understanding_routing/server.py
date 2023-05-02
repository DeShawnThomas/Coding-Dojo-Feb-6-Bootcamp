from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>') # for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
def say(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<string:word>') # for a route '/repeat/
def repeat(num, word):
    print(num, word)
    return (num * word)

#Sensei Bonus
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

