from flask import Flask, render_template, request
import model as m
from PIL import Image

# Author Naveenprabaharan S - GCT[1918L12]

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello():
    if request.method == "POST":
        original = request.files['original']
        oo = original
        tampered = request.files['tampered']
        Document_Tampering_Detection , score = m.Document_Tampering_Detection(original,tampered)
        score = score
        dcp = Document_Tampering_Detection
        print(dcp)
    return render_template("index.html", pred=dcp, score = score)


@app.route("/")
def submit():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

"""
@app.route("/sub", methods = ["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form['username']

    # .py -> HTML
    return render_template("sub.html", n = name)
"""
