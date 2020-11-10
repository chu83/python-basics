#객체의 대소 비교
print(1>3)
print(2>4)
print(1 >= 3)
print(1 == 3)
print(1 != 3)

#복합 관계식
a = 4
print(0 < a and a < 10)
print(0 < a < 10)

#다른타입
print('abcd' < 'abcde')
print('aac' > 'abc')
print((1,2,3))

#동질성
a = 20
b = 20
c = a

print(a==b)
print(a is b)
print(a is c)
print(a == c)