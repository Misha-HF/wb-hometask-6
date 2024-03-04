
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
select s.name as subject_name, ROUND(AVG(g.grade), 2) as AVG_grade_sub
from grades g
join subjects s on g.subject_id = s.id
where s.id = 3
group by s.id 
"""

print(execute_query(sql))