from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["full-name"]
        email = request.form["email"]
        message = request.form["message"]
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5550)