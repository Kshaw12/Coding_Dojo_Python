# for all the routes

from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def first_route():
    return redirect('/index')

# display #page1
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/submit_form', methods=['post'])
def form_submit():
    print(f"\n\n\nThe form being submitted: {request.form}\n\n\n")
    User.save(request.form)
    return redirect('/show')

# display #page2
@app.route('/show')
def show():
    user2 = User.get_all()
    print(user2)
    return render_template("show.html", users=user2)