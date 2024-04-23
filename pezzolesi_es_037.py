from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("pezzolesi_es_037.json") as f:
        data = json.load(f)
    return render_template("pezzolesi_es_37.html",links = data)


if __name__ == "__main__":
    app.run(debug=True, port=6946)
