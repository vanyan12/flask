from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return "Hello"
=======
    return "Hel"
>>>>>>> bc7a2e1a8b4d09d9ea4cc7b79d30ca881a54df16


if __name__ == "__main__":
    app.run(debug=True)
