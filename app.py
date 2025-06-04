import mysql.connector
from flask import Flask, request, render_template, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = 'SCRETKAY'

def get_db_connection():
    return mysql.connector.connect(
        host = "10.2.3.63",
        user = "Max@%",
        password = "AX-d120",
        database = "arsdatabase",
        charset = "utf8mb4",
        collation = "utf8mb4_general_ci"
    )


@app.route("/")
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user and check_password_hash(user[2], password):
            session.permanent = True
            session["email"] = email
            return redirect(url_for("website"))
        else:
            session["email"] = email
            return "Wrong email or password"
    else:
        return render_template("index.html")


@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user_name = request.form["user_name"]

        hashed_password = generate_password_hash(password, method='scrypt')

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return "email alredy registered"

        cursor.execute(
            "INSERT INTO users (email, password, user_name) "
            "VALUES (%s, %s, %s)",
            (email, hashed_password, user_name)
        )
        db.commit()
        cursor.close()
        db.close()

        session["email"] = email
        return redirect(url_for("website"))
    return render_template("register.html")

@app.route("/website", methods = ["GET", "POST"])
def website():
    if "email" in session:
        return render_template("website.html")
    else:
        return redirect(url_for("login"))

@app.route("/profile")
def profile():
    if "email" not in session:
        return redirect(url_for("login"))
    
    db = get_db_connection()
    Cursor = db.cursor()

    Cursor.execute("SELECT user_name FROM users WHERE email = %s", (session["email"],))

    user = Cursor.fetchone()
    db.close()
    Cursor.close()

    if user:
        return render_template("profile.html", username = user[0])
    else:
        return "User not found"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)