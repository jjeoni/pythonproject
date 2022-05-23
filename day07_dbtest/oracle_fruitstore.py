import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '192.168.1.26:1521/xe')
cursor = conn.cursor()

cursor.execute("drop table fruit_store")
cursor.execute("create table fruit_store(fruit_name varchar2(20), price number(7), count number(3))")

while True:
    choice = input('''1.입력 2.수정 3.삭제 4.확인 5.종료
        번호를 선택하세요 >>> ''')
    
    if choice == '1':
        sql = "insert into fruit_store values (:1, :2, :3)"
        cursor.execute('select * from fruit_store')

        for item in cursor:
            print(item[0], item[1], item[2])
        fruit_name = input('과일명 >>> ')
        price = input('가격 >>> ')
        count = input('수량 >>> ')
        data = (fruit_name, int(price), int(count))
        cursor.execute(sql, data)
        cursor.close
        conn.commit()       


    elif choice == '2':
        cursor.execute('select * from fruit_store')
        for item in cursor:
            print(item[0], item[1], item[2])

        fruits = input('수정할 과일 이름 >>> ')
        modify_num = input('수정할 항목 (1. 가격 2. 개수) >>> ')
        if modify_num == "1":
            price2 = input('변경할 가격 >>> ')
            cursor.execute(f"update fruit_store set price = '{price2}' where fruit_name = '{fruits}'")
        elif modify_num == "2":
            count2 = input('변경할 수량 >>> ')
            cursor.execute(f"update fruit_store set count = '{count2}' where fruit_name = '{fruits}'")
        cursor.close
        conn.commit()


    elif choice == '3':
        cursor.execute('select * from fruit_store')
        for item in cursor:
            print(item[0], item[1], item[2])

        delete_name = input('삭제할 과일 이름 >>> ')
        cursor.execute(f"delete from fruit_store where fruit_name = '{delete_name}'")
        for item in cursor:
            print(item[0], item[1], item[2])
        cursor.close
        conn.commit()


    elif choice == '4':
        cursor.execute("select * from fruit_store")
        for item in cursor:
            print(item[0], item[1], item[2])
        cursor.close
        conn.commit()


    elif choice == '5':
        print('프로그램을 종료합니다')
        conn.close()
        break