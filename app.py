import mysql.connector
from flask import Flask, request, render_template, session


app = Flask(__name__)

app.secret_key = 'SCRETKAY'

def get_db_connection():
    return mysql.connector.connect(
        host = "10.2.2.245",
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

@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user_name = request.form["user_name"]

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
        if cursor.fetchone():
            return "email alredy registered"

        cursor.execute(
            "INSERT INTO customers (email, password, full_name) "
            "VALUES (%s, %s, %s)",
            (email, password, user_name)
        )
        db.commit()
        cursor.close()
        db.close()

        session["email"] = email
        return redirect(url_for("store"))
    return render_template(register.html)


    if __name__ == "__main__":
        app.run(debug=True)