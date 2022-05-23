import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '192.168.1.26:1521/xe')
cursor = conn.cursor()

cursor.execute("drop table fruit_store")
cursor.execute("create table fruit_store(fruit_name varchar2(20), price number(7), count number(3))")
# sql = "insert into fruit_store values (:1, :2, :3)"

# fruit_name = input('과일명 >>> ')
# price = input('가격 >>> ')
# count = input('수량 >>> ')
# data = (fruit_name, int(price), int(count))
# cursor.execute(sql, data)

fruits = [('키위', 3000, 4), ('포도', 5000, 5), ('딸기', 8000, 6), ('귤', 7000, 7)]
sql = "insert into fruit_store values (:1, :2, :3)"
fruit_name = input('과일명 >>> ')
price = input('가격 >>> ')
count = input('수량 >>> ')
data = (fruit_name, int(price), int(count))

for row in fruits:
    cursor.execute(sql, row)
cursor.execute(sql, data)


sql2 = 'select * from fruit_store'
cursor.execute(sql2)
for i in cursor:
    print(i[0:3])

price2 = int(input('수정할 가격 >>> '))



# sql3 = "delete from fruit_store where fruit_name = '수박'"
# cursor.execute(sql3)
# for i in cursor:
#     print(i[0:3])


# cursor.execute("update fruit_store set price = 5500 where fruit_name = '수박'")
# cursor.execute("delete from fruit_store where fruit_name = '수박'")


cursor.close()
conn.commit()
conn.close()