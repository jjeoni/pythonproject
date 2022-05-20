from operator import itemgetter

def fruit_input(fruitlist):
    print('--------------현재 재고현황---------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('------------------------------------------')
    fruitl = {'fruit' : '', 'price' : '', 'stock' : ''}
    while True:
        fruitl['fruit'] = input('추가할 과일명을 입력하세요. >>> ')
        check = 0
        for i in fruitlist:
            if i['fruit'] == fruitl['fruit']:
                check = 1
                break
        if check == 0:
            break
        print('중복되는 과일이 존재합니다.')
    price = 'a'
    while not fruitl['price'].isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요. >>> ')
        break
    fruitl['price']=int(price)
    stock = 'b'
    while not fruitl['stock'].isdecimal():
        stock = input('추가할 메뉴의 수량을 입력하세요. >>> ')
        break
    fruitl['stock']=int(stock)
    fruitlist.append(fruitl)
    print('--------------추가된 재고현황---------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('--------------------------------------------')


def fruit_sale(fruitlist):
    print('--------------현재 재고현황---------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('--------------------------------------------')

    while True:
        choice1 = input('판매한 과일을 입력하세요 (종료 : Q) : ').upper()
        idx = -1
        for i in range(len(fruitlist)):
            if fruitlist[i]['fruit'] == choice1:
                idx = i
                break
        if idx == -1:
            print('등록되어있지 않은 과일입니다.')
            break
        
        choice2 = input('판매한 수량을 입력하세요 : ')         
        
        stock2 = int(fruitlist[i]['stock'])
        stock2 -= int(choice2)
        if stock2 < 0:
            s = fruitlist[i]['stock']
            print('재고가 없습니다')                   
        else:
            fruitlist[i]['stock']=stock2
        break


def fruit_list(fruitlist):
    fruitlist = sorted(fruitlist, key=itemgetter('stock'), reverse=True)
    print('----------------재고 리스트-----------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('--------------------------------------------')


def fruit_delete(fruitlist):
    print('--------재고 없음--------')
    for idx in range(len(fruitlist)):
        if fruitlist[idx]['stock'] == 0:
            print(fruitlist[idx])
    print('--------재고 있음--------')
    for idx in range(len(fruitlist)):
        if fruitlist[idx]['stock'] != 0:
            print(fruitlist[idx])
    print('-------------------------')
