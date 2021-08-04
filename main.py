from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/main")
def home_page():
    return render_template("home_page.html")


@app.route("/market")
@app.route("/shop")
def market_page():
    return render_template("market_page.html")
