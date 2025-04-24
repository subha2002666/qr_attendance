import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

# Drop old table if it exists
cursor.execute('DROP TABLE IF EXISTS attendance')

# Create new table with 'month' column
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        student_id TEXT,
        timestamp TEXT,
        month TEXT
    )
''')

conn.commit()
conn.close()
print("Database and table created successfully.")
