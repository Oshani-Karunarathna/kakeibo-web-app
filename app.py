from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database path
DB_PATH = os.path.join("database","database.db")

# Database connection fuction
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Dashboard route
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# Add Expense Route
@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        
        date = request.form.get("date")
        category = request.form.get("category")
        description = request.form.get("description")
        amount = request.form.get("amount")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
            (date, category, description, amount)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_expense.html")


if __name__ == "__main__":
    app.run(debug=True)
