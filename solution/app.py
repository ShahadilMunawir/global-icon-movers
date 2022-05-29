from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("Database.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Contact('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Full Name' TEXT NOT NULL, 'Email' TEXT NOT NULL, 'Message' TEXT NOT NULL);")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["full-name"]
        email = request.form["email"]
        message = request.form["message"]
        cursor.execute("INSERT INTO Contact('Full Name', 'Email', 'Message') VALUES (?, ?, ?);", (name, email, message))
        db.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5550)