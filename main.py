import cv2
import sqlite3
from datetime import datetime
from tkinter import messagebox, Tk

# Hide Tkinter root window
root = Tk()
root.withdraw()

# Connect to SQLite database
conn = sqlite3.connect('database/attendance.db')
cursor = conn.cursor()

# Initialize OpenCV QR Code detector
qr_detector = cv2.QRCodeDetector()

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("QR Attendance Scanner started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Detect and decode QR Code
    data, bbox, _ = qr_detector.detectAndDecode(frame)

    if data:
        print(f"QR Code Data: {data}")
        try:
            name, student_id = data.split(",")
        except ValueError:
            print("Invalid QR Code format. Use 'Name,ID'")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check if already marked today
        cursor.execute("SELECT * FROM attendance WHERE student_id = ? AND date(timestamp) = date(?)",
                       (student_id.strip(), timestamp))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Attendance", f"{name.strip()}'s attendance is already marked today.")
        else:
            # Insert attendance record
            cursor.execute("INSERT INTO attendance (name, student_id, timestamp) VALUES (?, ?, ?)",
                           (name.strip(), student_id.strip(), timestamp))
            conn.commit()
            messagebox.showinfo("Attendance", f"Attendance marked for {name.strip()}!")

    # Display webcam frame
    cv2.imshow("QR Attendance Scanner", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
conn.close()
