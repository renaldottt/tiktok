from flask import Flask, render_template, redirect, request, url_for
from proc.proses import Tiktok

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def index_post():
    url = request.form["url"]
    if not url:
        return redirect(url_for("index"))

    tiktok = Tiktok(url)
    if tiktok.user() == "Error":
        return render_template("err.html")
    return render_template("success.html", image=tiktok.image(), standar=tiktok.standard(), hd=tiktok.hd(), name=tiktok.user())

@app.errorhandler(404)
def notfound():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)
