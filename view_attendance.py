import sqlite3
from collections import Counter
from datetime import datetime

# Connect to database
conn = sqlite3.connect('database/attendance.db')
cursor = conn.cursor()

# Define which year you want to see
year_to_check = '2025'

# Fetch all records for that year
cursor.execute("SELECT name, timestamp FROM attendance WHERE strftime('%Y', timestamp) = ?", (year_to_check,))
records = cursor.fetchall()

if records:
    # Count attendance per person
    attendance_count = Counter([record[0] for record in records])

    print(f"\n📊 Attendance Summary for Year {year_to_check}")
    print("-" * 40)
    print(f"{'Name':<20} | {'Attendance Count'}")
    print("-" * 40)
    for name, count in attendance_count.items():
        print(f"{name:<20} | {count}")
    print("-" * 40)
else:
    print(f"No attendance records found for {year_to_check}.")

# Close connection
conn.close()
