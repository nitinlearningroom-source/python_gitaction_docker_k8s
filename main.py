from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():

    conn = psycopg2.connect(
        host="postgres-service",
        database="sampledb",
        user="postgres",
        password="postgres123"
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT text FROM messages LIMIT 1"
    )

    row = cur.fetchone()

    conn.close()

    return row[0]