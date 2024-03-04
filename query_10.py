
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
sql = """
select distinct s2.fullname as student_name, g2.fullname as teacher_name, g2.sub as subject_name
from (select g.student_id, s1.fullname, s1.sub from (select t.fullname, s.id, s.name as sub from teachers t join subjects s on s.teacher_id = t.id where t.id = 1) as s1 
join grades g on s1.id = g.subject_id) as g2
join students s2 on g2.student_id = s2.id where s2.id = 20; 

"""

print(execute_query(sql))