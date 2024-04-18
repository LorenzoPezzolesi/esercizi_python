from flask import Flask, render_template
import json

app = Flask(__name__)


def index():
    with open("esercizio_037.json") as f:
        data = json.load(f)
    return render_template("dinamic.html",links = data)


if __name__ == "__main__":
    app.run(debug=True, port=6946)
