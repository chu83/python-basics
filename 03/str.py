print('================Multi-line==================')

s1 = 'Hello'
s2 = "Hello"
print(s1, type(s1), type(s2))

s3 = """Hello
world
"""
print(s3)

#escape(\)
print('================escape==================')
print('Hello\nworld')
print('I say "Hello"')
print('I say \'Hello\'')
print('둘리 \t 010-000-0000')

print('================문자열 연산:반복==================')
str1 = 'First String\t'
str2 = 'Second String'
print(str1*3)

print('================문자열 연산:인덱싱==================')
print(str1[0], str1[2], str1[3])

print('================문자열 연산:연결==================')
str4 = str1+str2
print(str4)
str5 = 'hello''   ''world'
print(str5)

#문자열과 정수는 + 연산 안됨


print('================문자열 연산:in, not in==================')
print("s" in str1)
print("S" not in str2)

print('================문자열 객체는 변경할 수 없다==================')

print('================문자열 연산:포맷팅==================')
epoch = 1000
init = (0,0)
diff = 10
"epoch=" + str(100) + "회 초기값" + str(init)
f'epoch={epoch}회'


print('================문자열 연산:슬라이싱==================')
str6 = str2[3:5]
print(str6)

str7 = str2[2:]
print(str7)

str8 = str2[:]
print(str8)


print('================문자열 연산:객체 함수==================')
#대소문자
s = "I like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

#검색
s = "I Like Python, I Like Deep Learning Also"
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))

print(s.find("AI"))
print(s.rfind("Like"))

try:
    print(s.index("AI"))
except ValueError as e:
    print("Sorry")
    print(e)

print(s.rindex("Like"))
print(s.startswith("I Like"))
print(s.endswith("Also"))
print(s.endswith("Python", 0, 13))

#편집
s='            spam and ham    '
print('----' + s.strip() + '----')
print('----' + s.rstrip() + '----')
print('----' + s.lstrip() + '----')

s='<><><abc><><defg><><>'
print('----' + s.strip('<>') + '----')

s='Hello Python Python Python'
print(s.replace('Python', 'Java'))

#분리
s = 'one:two:three'
r = s.split(':')
print(r, type(r))













