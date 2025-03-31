import mysql.connector
from flask import Flask, request, render_template, session


app = Flask(__name__)

app.secret_key = 'SCRETKAY'

def get_db_connection():
    return mysql.connector.connect(
        host = "10.2.2.245",
        user = "Max@%",
        password = "AX-d120",
        database = "",
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

        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            session.permanent = True
            session["email"] = email
            return redirect(url_for("mainpage"))
        else:
            session["email"] = email
            return "Wrong email or password"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)