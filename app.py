import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("cats.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS cats (id INTEGER PRIMARY KEY, name TEXT, owner TEXT)"
    )
    return conn


@app.route("/cats")
def find_cat():
    owner = request.args.get("owner", "")
    conn = get_db()
    # Vulnerable: user input concatenated directly into the query (SQL injection)
    query = "SELECT * FROM cats WHERE owner = '" + owner + "'"
    rows = conn.execute(query).fetchall()
    return {"cats": rows}


if __name__ == "__main__":
    app.run(debug=True)
