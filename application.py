import datatime

from flask import Flask, render_template, request, session

form flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.comfig["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods = ["GET", "POST"])
def index():
  if session.get("notes") is None:
    session["notes"] = []
  if request.method == "POST":
    note = request.form.get("note")
    session["notes"].append(note)
  return render_template("index.html", notes = session["notes"])

