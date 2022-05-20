import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '192.168.1.26:1521/xe')
cursor = conn.cursor()
cursor.execute('select * from emp')

print(cursor)

for item in cursor:
    print(item[0:8])

# conn.close()

# cursor.execute('select job from emp')
