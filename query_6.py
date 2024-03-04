import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти список студентів у певній групі.
sql = """
select s.id, s.fullname, groups.name as group_name
from students s join groups on s.group_id = groups.id
where groups.id = 2 
"""

print(execute_query(sql))
