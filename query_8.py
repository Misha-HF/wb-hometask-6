
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
select ROUND(AVG(g.grade), 2) AS average_grade
from (select sub.id from subjects sub join teachers t on sub.teacher_id = t.id where t.id = 2) as teacher_sub
join grades g on teacher_sub.id = g.subject_id
"""

print(execute_query(sql))