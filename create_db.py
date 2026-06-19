import sqlite3

conn = sqlite3.connect('app.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    text TEXT
)
""")

cursor.execute("DELETE FROM messages")

cursor.execute("""
INSERT INTO messages(text)
VALUES('Hello from SQLite Database in Kubernetes!')
""")

conn.commit()
conn.close()

print("Database created")