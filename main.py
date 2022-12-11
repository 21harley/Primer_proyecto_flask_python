from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello_wordl():
    return render_template("index.html")