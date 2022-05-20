from flask import Flask
import random
app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "Why did the security conscious engineer refuse to pay their dinner bill? Because they could not verify the checksum."
]

@app.route("/") #Video uses a get method but this did not work on our system.
def tell_a_Joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"