from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hel():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
