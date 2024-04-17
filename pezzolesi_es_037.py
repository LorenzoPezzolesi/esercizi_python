from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    return ""


@app.route("/dati_grezzi/")
def dati_grezzi():
    with open("votes.json") as f:
        data = json.load(f)
    return data

@app.route("/dati_formattati/")
def dati_formattati():
    with open("votes.json") as f:
        data = json.load(f)
    result = ''
    for student in data:
        result += f"{student['name']} ha preso {student['vote']}"
        result += "<br>"
    return result


@app.route("/table/")
def table():
    with open("votes.json") as f:
        data = json.load(f)
    return render_template("table.html", students=data)


if __name__ == "__main__":
    app.run(debug=True, port=1234)

#def carica_il_file():












