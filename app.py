# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Vigya" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():
    name = "Rajneesh"
    age = "49"
    relation = "Father"

    return render_template('father.html' , name = name, age = age, relation = relation)
# define the route to mother webpage
@app.route("/mother")
def mother_webpage():
    name = "Archana"
    age = "49"
    relation = "Mother"

    return render_template('mother.html' , name = name, age = age, relation = relation)

# define the route to friends webpage
@app.route("/friend")
def friend_webpage():
    name = "Pragya"
    age = "19"
    relation = "Friend"

    return render_template('friend.html' , name = name, age = age, relation = relation)


# define the route to sister webpage
@app.route("/sister")
def sister_webpage():
    name = "Harshita"
    age = "9"
    relation = "Sister"

    return render_template('sister.html' , name = name, age = age, relation = relation)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
