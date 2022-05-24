import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '192.168.1.4:1521/xe')
cursor = conn.cursor()

cursor.execute("drop table fruit_store")
cursor.execute("create table fruit_store(fruit_name varchar2(20), price number(7), count number(3))")

while True:
    choice = input('''1.입력 2.수정 3.삭제 4.확인 5.종료
        번호를 선택하세요 >>> ''')
    
    if choice == '1':
        sql = "insert into fruit_store values (:1, :2, :3)"
        cursor.execute('select * from fruit_store')
        print('--------------------------------------------')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        fruit_name = input('추가할 과일명을 입력하세요 >>> ')
        price = input('추가할 과일의 가격을 입력하세요 >>> ')
        count = input('추가할 과일의 수량을 입력하세요 >>> ')
        data = (fruit_name, int(price), int(count))
        cursor.execute(sql, data)
        print('--------------------------------------------')
        cursor.execute('select * from fruit_store')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        cursor.close
        conn.commit()       


    elif choice == '2':
        cursor.execute('select * from fruit_store')
        print('--------------현재 재고현황---------------')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')

        fruits = input('수정할 과일 이름을 입력하세요 >>> ')
        modify_num = input(''' 다음 중 수정할 항목을 선택하세요
        price, count 중 입력 >>> ''')
        if modify_num == "prcie":
            price2 = input('변경할 가격을 입력하세요 >>> ')
            cursor.execute(f"update fruit_store set price = '{price2}' where fruit_name = '{fruits}'")
        elif modify_num == "count":
            count2 = input('변경할 수량을 입력하세요 >>> ')
            cursor.execute(f"update fruit_store set count = '{count2}' where fruit_name = '{fruits}'")
        else :
            print('다시 입력하세요')
        print('--------------------------------------------')
        cursor.execute('select * from fruit_store')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        cursor.close
        conn.commit()


    elif choice == '3':
        cursor.execute('select * from fruit_store')
        print('--------------현재 재고현황---------------')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        delete_name = input('삭제할 과일 이름을 입력하세요 >>> ')
        cursor.execute(f"delete from fruit_store where fruit_name = '{delete_name}'")
        print(f'<<<<<<<<<{delete_name}이 삭제되었습니다.>>>>>>>>>')
        cursor.execute('select * from fruit_store')
        print('--------------삭제 후 재고현황---------------')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        cursor.close
        conn.commit()


    elif choice == '4':
        cursor.execute("select * from fruit_store")
        print('----------------재고 리스트-----------------')
        for item in cursor:
            print(f'{item[0]} {item[1]}원 {item[2]}개')
        print('--------------------------------------------')
        cursor.close
        conn.commit()


    elif choice == '5':
        print('프로그램을 종료합니다')
        conn.close()
        break