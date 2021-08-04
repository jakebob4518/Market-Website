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
    
    items = [{'id': 1, 'name': 'Cell Phone', 'barcode': '873521659011', 'price': 500},
             {'id': 2, 'name': 'Laptop', 'barcode': '723560192311', 'price': 750}]
    
    return render_template("market_page.html", items=items)
