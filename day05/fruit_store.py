# 과일가게 재고 프로그램
# - 1.입력 : 딕셔너리{과일명, 가격, 재고}, 과일 추가(중복 불가)
# - 2.판매 : 데이터를 입력받아서 남은 재고 출력, q 입력시 입력 종료
# - 3.재고리스트 : 재고를 기준으로 내림차순 정렬 후 출력
# - 4.삭제 : 재고가 0이면 재고가 없다는 메세지 출력 후 남은 재고리스트 출력,
#            데이터를 삭제하기 보다는 재고가 있는 것과 재고가 없는 것을 기준으로 나누고 따로 출력
# - 5.종료 : 프로그램 종료

# 어려웠던 점 : 판매부분에서 재고가 없는 과일을 입력할 때 재고가 없다는 메세지 출력이 어려웠움


import json
import fruit_store_function as fsf

# f = open('fruit_store.json', 'r')
# fruitlist = json.load(f)
# f.close()

fruitlist = [{'fruit': '수박', 'price': '8000', 'stock' : 5},
             {'fruit': '청포도', 'price': '7000', 'stock' : 6},
             {'fruit': '딸기', 'price': '7500', 'stock' : 10}]
while True:
    choice = input('''1.입력 2.판매 3.재고리스트 4.삭제 5.종료
번호를 선택하세요 >>> ''')
    
    if choice == '1':
        fsf.fruit_input(fruitlist)

    elif choice == '2':
        fsf.fruit_sale(fruitlist)

    elif choice == '3':
        fsf.fruit_list(fruitlist)

    elif choice == '4':
        fsf.fruit_delete(fruitlist)

    elif choice == '5':
        print('프로그램을 종료합니다')
        f = open('fruit_store.json', 'w')
        json.dump(fruitlist, f)
        f.close()
        break

    else:
        print('잘못 입력하였습니다. 다른 번호를 입력하세요')
