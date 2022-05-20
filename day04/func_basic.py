def menu_input(menu):
    print('현재 메뉴 : ', list(menu.keys()))
    name = input('추가할 메뉴명 : ')
    price = 'a'
    while not price.isdecimal():
        price = input('추가할 메뉴의 가격 : ')
    menu[name] = int(price)

def menu_modify(menu):
    print('현재 메뉴 : ', list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('수정할 메뉴명 : ')
    price = 'a'
    while not price.isdecimal():
        price = input('수정할 메뉴의 가격 : ')
    menu[name] = int(price)

def menu_confirm(menu):
    print('----------------------menu----------------------')        
    for item in sorted(menu.items(), key=lambda data:data[1]): # 가격순으로 바꾸고 싶다면 data:data[1]/ 내림차순 data:data[1], reverse=True  
        print(f'{item[0]} : {item[1]:,}')

def menu_delete(menu):
    print('현재 메뉴 : ', list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('삭제할 메뉴명 : ')
    del menu[name]
    for item in menu.items():
        print(f'{item[0]} : {item[1]:,}')
