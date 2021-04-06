from flask import Flask, render_template, request, redirect # added request

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("request.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    language_from_form = request.form['language']
    location_from_form = request.form['location']
    return render_template("result.html", name_on_template=name_from_form, email_on_template=email_from_form,
    languge_on_template=language_from_form, location_on_template=location_from_form )


if __name__=="__main__":
    app.run(debug=True)    # Run the app in debug mode.