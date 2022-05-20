def test_func(a,b):
    '''
    함수를 작성합니다.
    함수에 대한 설명란(함수 독스트링)
    '''
    print('test_func함수 실행', a,b)

test_func(1,'a')

def add1():
    print(1+2)

def add2(a,b):
    print(a+b)

def add(c, a=1, b=2): # 디폴트값 설정
    print(a+b)
    return c, a, b

add(1)
add(1,4)
x = add(1, b=5, a=3)
print(x[1])
x,y,z = add(1, b=5, a=3)
print(x, y, z)