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



print('================문자열 연산:슬라이싱==================')










