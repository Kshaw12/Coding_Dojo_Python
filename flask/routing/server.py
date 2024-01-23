from flask import Flask  # Import Flask to allow us to create our app

# name of app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/')
def dojo():
    return 'Dojo'


@app.route('/say/<name1>/<name2>/<name3>')
def say_flask(name1, name2, name3):
    return (f" {name1}, Hi {name2}, Hi {name3}")

    # self.name1= 'Hi Flask'.self
    # self.name2= 'Hi Michael'
    # self.name3= 'Hi John'
    # return 'Hi Flask!' + name1 + name2 + name3


# Here the second parameter is cast into an integer before being passed to the function
@app.route('/repeat/<hello>/<int:num>') 
def hello1(hello, num):
    return f"Hello, {hello * num}"

@app.route('/repeat/<int:numm>/<byee>') 
def hello2(numm, byee):
    return f"{byee * numm}"

@app.route('/car/<int:number>/<dogs>') 
def hello3(dogs, number):
    return f"{dogs * number}"





# @app.route('/python/<name>')
# def python():
#     return 'python + name'



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

