from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return 'Hello' + ' '+ name.capitalize()+'!'
    # as long as variable name is between <> that means this is souposed to be a string

@app.route('/repead/<int:num>/<quote>')
def repead(num, quote):
    return num *(' '+quote)
 # as long as variable name is between <> that means this is souposed to be a string and variable is writtne int:variable name that means it is a intiger



 



if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.
