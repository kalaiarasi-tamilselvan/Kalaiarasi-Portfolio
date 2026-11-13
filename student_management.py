# Student Management System
# Python + SQLite (SQL database)
# Author: Kalaiarasi T

import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks REAL NOT NULL
)
""")
conn.commit()


def read_marks():
    while True:
        try:
            m = float(input("Marks (0-100): "))
            if 0 <= m <= 100:
                return m
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def add_student():
    name = input("Name: ").strip()
    course = input("Course: ").strip()
    if not name or not course:
        print("Name and course cannot be empty.")
        return
    marks = read_marks()
    cur.execute("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
                (name, course, marks))
    conn.commit()
    print("Student added.")


def show_rows(rows):
    if not rows:
        print("No records found.")
        return
    print(f"\n{'ID':<5}{'Name':<20}{'Course':<15}{'Marks':<8}")
    print("-" * 48)
    for r in rows:
        print(f"{r[0]:<5}{r[1]:<20}{r[2]:<15}{r[3]:<8}")


def view_all():
    cur.execute("SELECT * FROM students ORDER BY id")
    show_rows(cur.fetchall())


def search_student():
    key = input("Enter name to search: ").strip()
    cur.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + key + "%",))
    show_rows(cur.fetchall())


def update_marks():
    sid = input("Enter student ID: ")
    if not sid.isdigit():
        print("Invalid ID.")
        return
    marks = read_marks()
    cur.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, int(sid)))
    conn.commit()
    print("Marks updated." if cur.rowcount else "No student with that ID.")


def delete_student():
    sid = input("Enter student ID: ")
    if not sid.isdigit():
        print("Invalid ID.")
        return
    cur.execute("DELETE FROM students WHERE id = ?", (int(sid),))
    conn.commit()
    print("Student deleted." if cur.rowcount else "No student with that ID.")


def report():
    cur.execute("SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students")
    count, avg, high, low = cur.fetchone()
    if count == 0:
        print("No records yet.")
        return
    print(f"\nTotal students : {count}")
    print(f"Average marks  : {avg:.2f}")
    print(f"Highest marks  : {high}")
    print(f"Lowest marks   : {low}")
    cur.execute("SELECT name FROM students WHERE marks = ?", (high,))
    print("Topper(s)      :", ", ".join(r[0] for r in cur.fetchall()))
    print("\nCourse-wise average:")
    cur.execute("SELECT course, AVG(marks) FROM students GROUP BY course")
    for course, a in cur.fetchall():
        print(f"  {course}: {a:.2f}")


def main():
    actions = {
        "1": add_student, "2": view_all, "3": search_student,
        "4": update_marks, "5": delete_student, "6": report,
    }
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search by name")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Report (average, topper)")
        print("7. Exit")
        choice = input("Choose (1-7): ")
        if choice == "7":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")
    conn.close()


main()
