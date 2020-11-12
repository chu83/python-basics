#for loop

print('========== for loop 기본 ===========')
a=['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')


print('========== 복합 자료형의 for loop ===========')
l1 = [('둘리', 10), ('마이콜', 20), ('또치', 10)]
for t in l1:
    #print(f'이름 : {t[0]}, 나이 : {t[1]}')
    print('이름 : %s, 나이 : %d' %t)


print('========== 1~10 합 ===========')
sum = 0
for i in range(1, 11):
    sum = sum+i

print(sum)

#break
for i in range(10):
    if i>5:
        break
    print(i, end=' ')
else:
    print('--end loop\n')

print('========== continue ===========')
for i in range(10):
    if i <= 5 :
        continue
    print(i, end=' ')
else:
    print('--end loop\n')

print('========== 삼각형 ===========')
for i in range(0, 5):
    for j in range(0,i+1):
        print('*', end='')
    print("")
print('========== 역삼각형 ===========')
for i in range(10, 1, -1):
    if i <= 10:
        star = '*' * i
        print(star)


print('========== 정삼각형 ===========')
for i in range(1,10):
    if i <= 10:
        star = '*' * i
        vacant = ' '* (10-i)

        print(star+vacant)


print('========== 구구단 ===========')
for i in range(1,10):
    for j in range(1, 10):
        print(f'{j} * {i} = {i*j} ', end='\t')
    print(end='\n')












