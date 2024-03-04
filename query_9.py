
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
select distinct  w.fullname, s1.name as subject_name
from (select s.fullname, g.subject_id from students s join grades g on g.student_id =s.id where s.id = 20) as w
right join subjects s1 on w.subject_id = s1.id; 

"""

print(execute_query(sql))