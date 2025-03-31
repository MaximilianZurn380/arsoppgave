import mysql.connector
from flask import Flask, render_template


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

if __name__ == "__main__":
    app.run(debug=True)