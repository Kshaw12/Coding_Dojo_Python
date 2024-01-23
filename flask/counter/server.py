from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"

@app.route('/')         
def index():
    if 'total_count' in session:
        session['total_count'] += 1
        print('key exists!')
    else:
        session['total_count'] = 1 
        print("key 'key_name' does NOT exist")
    # session['added'] = session.get('added', 0)
    return render_template('index.html')

@app.route('/eliminate_session', methods= ['GET', 'POST'])
def eliminate():
    session.clear()
    return redirect("/")

@app.route('/add_two',methods= ['GET', 'POST'])
def add_two():
    session['total_count']+=1
    return redirect("/")

@app.route('/add_any',methods= ['POST'])
def add_any():
    session['adder'] = request.form['adder']
    add_value=int(request.form['adder'])-1
    session['total_count']+=add_value
    return redirect("/")

if __name__ == '__main__':
    app.run()


# return render_template("index.html")