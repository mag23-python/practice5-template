from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/home/")
def home_page():
    name = request.args.get("name", "Вова")
    return render_template("home.html", name=name)
