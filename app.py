from flask import Flask, render_template, request
from data_fetcher import get_crypto_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        token = request.form["token"]
        result = get_crypto_data(token)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
