from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    cursor.execute("SELECT text FROM messages LIMIT 1")

    row = cursor.fetchone()

    conn.close()

    if row:
        return f"<h1>{row[0]}</h1>"

    return "<h1>No Data Found</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)