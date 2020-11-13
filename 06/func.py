#함수 정의
print('=========== 함수===========')

def dummy():
    pass

def func1():
    print("hello world")

def func2(name):
    print('hello' + name)

def func3():
    return 'hello world'

def times(a, b):
    return a*b

dummy()
func1()
func2('나다')
s= func3()
n = times(2, 2)
print(s,n)


print('=========== 여러 값을 반환===========')

def func4():
    return 10, 20 # tuple auto unpacking 을 통해 튜플 객체 하나 반환

a, b = func4()
print(a, b)

print('=========== 함수도 객체다 ===========')
print(func1)
print(type(func1))
f = func1
f()














