# pip install cx_Oracle
import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '192.168.1.26:1521/xe')
cursor = conn.cursor()
cursor.execute('select * from emp where deptno = 10')

# print(cursor)

for item in cursor:
    print(item[1], item[5])

conn.close()
