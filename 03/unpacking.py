#packing은 튜플로만 가능하다
t = 10, 20, 30, 'pypthon'
print(t, type(t))

#unpacking
a, b, c, d= t
print(a, b, c, d)

#unpacking 확장
t = (1,2,3,4,5)
a, *b = t
print(t)
print(a)
print(b)

def f1(*b):
    pass

def f2(a,b,c):
    pass

t=(1,2,3)
f2(*t)
print(t)