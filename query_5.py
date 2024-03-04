import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#знайти курси, які читає певний викладач
sql = """
select t.fullname, subjects.name as subject_name
from subjects join teachers t on subjects.teacher_id = t.id
where t.id = 3
"""

print(execute_query(sql))
