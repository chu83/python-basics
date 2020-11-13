#call by reference
#call by value

def f(i):
    i = 20

def f2(seq):
    seq[0] =10

a=10
print(a)
f(a)
print(a)

#컨테이너형 불변 객체를 파라미터로 사용
#내부에서 변경(오류
# t = (1, 20, 30, 40)
# a= list(t)
# f2(a)

#컨테이형 가변 객체를 파라미터로 사용
#내부에서 변경
l = [1, 20, 30, 40]
f2(l)
print(l)
















