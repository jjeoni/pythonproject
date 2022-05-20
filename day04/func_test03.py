def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('홍길동', 25, '대구')

# 딕셔너리 언팩킹
personal_info(**{'name' : '홍길동', 'address' : '대구', 'age' : 25})

def personal_info1(**info):
    # print(info)
    for k, v in info.items():
        print(k,v)

personal_info1(name='홍길동', address='대구', age=25, tel='111-2222')