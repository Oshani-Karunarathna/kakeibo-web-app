from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database path
#DB_PATH = os.path.join("database","database.db")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "database.db")
print("APP DB PATH:", DB_PATH)


# Database connection fuction
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Dashboard route
@app.route("/")
def dashboard():
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    total = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
    print("EXPENSES COUNT:", len(expenses))
    conn.close()
    return render_template("dashboard.html", expenses=expenses,total=total or 0,category_totals=[])

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
