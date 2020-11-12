# 문제1
# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요


try:
    number = int(input("수를 입력하세요 : "))
except ValueError as e:
   print("정수가 아닙니다.")
else:
    if number % 3 == 0:
        print("3의 배수 입니다.")
    else:
        print("3의 배수가 아닙니다.")

