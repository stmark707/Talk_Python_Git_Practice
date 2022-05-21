import flask
from flask import Flask
import random
from data import jokes

app = Flask(__name__)


@app.route("/") #Video uses a get method but this did not work on our system.
def tell_a_Joke():
    joke = random.choice(jokes)
    
    return flask.render_template('joke.html', joke_text=joke)
    
    #return f"<p>{joke}</p>"
    