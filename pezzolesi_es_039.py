from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("")
def flashcard(id):
    return render_template("pezzolesi_es_039.html")

