from flask import Flask,render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')
def test():
    return "Flask is setup!"

'''
Level 1
have it render three beautiful looking blue boxes. 
'''

@app.route('/play')
def blue_boxes():
    return render_template('index.html', number=3, color="blue")

'''
Level 2
When a user visits 'localhost:5000/play/(x)', 
have it display the beautiful looking blue boxes
 x times. 
'''
@app.route('/play/<int:num>')
def bluey(num):
    print(f"\n\n\n------------------->{num}")
    return render_template("index.html", number=num, color="red" )

"""
Level 3
When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). For example, localhost:5000/play/5/green would display 5 beautiful green boxes. Calling localhost:5000/play/35/red 
would display 35 beautiful red boxes.
"""
@app.route('/play/<int:num>/<clr>')
def redie(num,clr):
    print(f"\n\n\n------------------->{num}{clr}")
    return render_template("index.html", number=num, color=clr)




if __name__=="__main__":
    app.run(debug=True)







