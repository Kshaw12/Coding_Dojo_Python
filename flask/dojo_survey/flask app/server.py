from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "THIS CAN BE WHATEVER YOU WANTS"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods =['POST'])#ALWAYS RIDIRECT IN A POST ROUTE
def user_result():
    print("Got Post Info")
    session['name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')# IN A GET ROUTE YOU CAN EITHER RENDER A TEMPLATE OR REROUTE TO ANOTHER ROUTE
def show_result():
    if 'name'  not in session or 'location'  not in session or 'language'  not in session or 'comment' not in session:
         return redirect('/')
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)
