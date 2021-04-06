from flask import Flask, flash, request, redirect, url_for
@app.route('/')         
def index():
    return render_template("index.html")

if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

session.clear()		# clears all keys
session.pop('key_name')		# clears a specific key
if __name__=="__main__":   
    app.run(debug=True)    