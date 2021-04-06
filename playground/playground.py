from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello'
@app.route('/play')
def index():
    return render_template("index.html", times=5)	# notice the 2 new named arguments!


@app.route('/play/<int:times>')
def times(times):
    return render_template("index.html",num_times=times )	# notice the 2 new named arguments!


@app.route('/play/<int:times>/<color>')
def color(times, color):
    return render_template("index.html",num_times=times, colors=color )	
if __name__=="__main__":
    app.run(debug=True)
