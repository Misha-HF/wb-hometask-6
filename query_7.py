import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти оцінки студентів у окремій групі
#з певного предмета.
sql = """
SELECT student_group.fullname AS student_name, grade_subject.grade, student_group.group_name, grade_subject.subject_id
FROM (SELECT student.id, student.fullname, group_tbl.name AS group_name FROM students student JOIN groups group_tbl ON student.group_id = group_tbl.id  WHERE group_tbl.id = 2) AS student_group
JOIN (SELECT * FROM grades grade JOIN subjects subject ON grade.subject_id = subject.id WHERE subject.id = 1) AS grade_subject
ON grade_subject.student_id = student_group.id;


"""

print(execute_query(sql))