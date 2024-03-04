
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('create.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g JOIN students s ON s.id = g.student_id
where g.subject_id = 3
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
"""

print(execute_query(sql))