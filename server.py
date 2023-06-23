from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(1, 9)
print(random_number)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/18trqWNZnu33q/giphy.gif' />"


@app.route("/<int:guess>")
def guess_num(guess):
    if guess < random_number:
        return "<h1 style='color:blue'>Too low, pick another number!</h1>" \
                "<img src='https://media.giphy.com/media/7Jkv02RLFYj6M/giphy.gif' />"
    elif guess > random_number:
        return "<h1 style='color:pink'>Too high, pick another number!</h1>" \
                "<img src='https://media.giphy.com/media/jp2KXzsPtoKFG/giphy.gif' />"
    else:
        return "<h1 style='color:green'>Correct!</h1>" \
                "<img src='https://media.giphy.com/media/gVYk3rI8YjtAI/giphy.gif' />"


if __name__ == "__main__":
    app.run(debug=True)
