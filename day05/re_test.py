import re

# a = 'hello, world!'
# print(re.match('world', a))

# print(re.search('^hello', a))
# print(re.search('^world!', a))
# print(re.search('world!$', a))

# print(re.match('hello|world', a))

# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]+', str1))
# print(re.match('[0-9]*', str1))
# print(re.search('[0-9]*', str1))

# print(re.match('a*b', 'b'))
# print(re.match('a+b', 'b'))
# print(re.match('abc?d', 'abd'))
# print(re.match('ab[0-9]?c', 'ab3c'))
# print(re.match('ab.d', 'abxd'))

# print(re.match('h{3}', 'hhhello'))
# print(re.match('(hello){3}', 'hellohellohelloworld'))

# print(re.search('^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$', '02-100-10000 tel'))
# print(p.search('ss7up@gmail.com'))
# print(p.search('wlgus9214@naver.com'))

p =  re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''
while not p.search(email):
    email = input('email >>> ')

