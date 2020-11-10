#논리연산자(NOT, OR, AND)

a = 30
b1 = a <= 30
b2 = not b1

#논리합 or
b3 = a <= 30 or a >= 100

#논리곱 and
b4 = a <= 30 and a>=100


print(b1, b2)
print(not a <= 10)
print(b3)
print(b4)

print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([19, 20] or 'logical')
print('operator' or 'logicla')
print(None or 'logical')

s = 'Hello world'
#if s is not '':
#    print(s)
s and print(s)

s = ''
s and print(s)
print('------------------')