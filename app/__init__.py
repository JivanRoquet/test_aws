from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"


@app.route("/bye")
def bye():
    return "Bye bye cruel world!"


@app.route("/nice")
def nice():
    return "<h1>wow trop Nice Brice !!</h1>"


if __name__ == "__main__":
    app.run()
