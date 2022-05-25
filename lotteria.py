# 롯데리아 주문 관리 프로그램
# 1. 입력 : 거래일, 거래번호, 제품명, 단가, 수량, 금액
# 2. 수정 : 이벤트 할인 가격
# 3. 삭제 : 잘못 주문한 메뉴 삭제
# 4. 주문확인 : 총합계, 할인, 과세금액, 부가세액(10%), 청구액, 받은돈, 거스름돈, 포인트 적립(0.3% 적립) -> 판매한 영수증 모두 출력
# 5. 프로그램 종료

import re
import time

menulist = []

order_num = input('''
---------------------------------------
1.입력 2.수정 3.삭제 4.주문확인 5.종료
    원하시는 번호를 입력하세요 >>> ''') 

while True:
    if order_num == '1':
        while True:
            date1 = time.strftime('%Y/%m/%d/%a %H:%M:%S')
            product = input('제품명을 입력하세요 >>> ')
            price = int(input('단가를 입력하세요 >>> '))
            count = int(input('수량을 입력하세요 >>> '))

    elif order_num == '2':
        pass
    elif order_num == '3':
        pass
    elif order_num == '4':
        pass
    elif order_num == '5':
        pass
    else:
        pass

