from flask import Flask,  render_template # Import Flask to allow us to create our app
app = Flask(__name__) 

@app.route('/')

def render_lists():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},0
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
 
    return render_template("index.html", user=users)



if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.