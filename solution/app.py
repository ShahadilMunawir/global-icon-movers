from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = "complikeysecret#"
app.permanent_session_lifetime = timedelta(seconds=600)

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

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" in session:
        username = session["username"]
        flash(f"You are logged in as {username}")
        cursor.execute("SELECT * FROM Contact")
        data = cursor.fetchall()
        return render_template("admin.html", data=data)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "Shahadil" and password == "root@shahadil121#" or username == "Bodhi" and password == "bodhi_bo121":
            session["username"] = username
            return redirect(url_for("admin"))
        else:
            flash("Username or password is incorrect")
    else:
        if "username" in session:
            return redirect(url_for("admin"))
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5501)