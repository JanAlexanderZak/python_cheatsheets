from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/more")
def more():
    # use {{ url_for('more') }} in html code. Function to call function.
    return render_template("more.html")


app.run()
