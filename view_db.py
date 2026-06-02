import sqlite3
import json

conn = sqlite3.connect("skillpath.db")
cursor = conn.cursor()

print("\n===== JOB ROLES IN DATABASE =====")
cursor.execute("SELECT id, role_name FROM job_roles")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Role: {row[1]}")

print("\n===== USER RESULTS IN DATABASE =====")
cursor.execute("SELECT * FROM user_results")
rows = cursor.fetchall()
if rows:
    for row in rows:
        print(f"\nID: {row[0]}")
        print(f"Job Role: {row[1]}")
        print(f"Match Score: {row[4]}%")
        print(f"Matched Skills: {row[2]}")
        print(f"Missing Skills: {row[3]}")
        print(f"Date: {row[5]}")
else:
    print("No results yet! Analyze a resume first.")

conn.close()