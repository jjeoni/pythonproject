import func_basic as fb

menu ={'아아':3000, '라떼':4000, '코코아':3500}
while True:
    menunum = input('''
--------------------------------------------------------
1.메뉴입력 2.메뉴수정 3.메뉴목록 4.메뉴삭제 5.프로그램 종료
--------------------------------------------------------
                메뉴 선택 >>> ''')
    if menunum == '1':
        fb.menu_input(menu)
        
    elif menunum == '2':
        fb.menu_modify(menu)
        
    elif menunum == '3':
        fb.menu_confirm(menu)

    elif menunum == '4':
        fb.menu_delete(menu)
        
    elif menunum == '5':
        print('프로그램 종료')
        break
        
    else:
        print('메뉴를 잘못 선택하셨습니다.')