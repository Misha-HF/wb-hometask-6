import logging
import random
import sqlite3
from faker import Faker

fake = Faker()

def populate_database():
    # Встановлюємо з'єднання з базою даних SQLite
    conn = sqlite3.connect('create.db')
    cur = conn.cursor()

    # Заповнюємо таблицю groups
    for _ in range(3):
        cur.execute("INSERT INTO groups (name) VALUES (?)", (fake.word(),))

    # Заповнюємо таблицю teachers
    for _ in range(3):
        cur.execute("INSERT INTO teachers (fullname) VALUES (?)", (fake.name(),))

    # Заповнюємо таблицю subjects
    for teacher_id in range(1, 4):
        for _ in range(2):
            cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake.word(), teacher_id))

    # Заповнюємо таблицю students
    for group_id in range(1, 4):
        for _ in range(10):
            cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?)", (fake.name(), group_id))
            student_id = cur.lastrowid
            for subject_id in range(1, 7):
                for _ in range(3):
                    cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                                (student_id, subject_id, random.randint(0, 100), str(fake.date_this_decade())))

    # Зберігаємо зміни та закриваємо з'єднання з базою даних
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_database()
