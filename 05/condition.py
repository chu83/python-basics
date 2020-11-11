#if ~ else
a=1
if a > 5:
    print('big')

else:
    print('small')

#if ~ elif ~ else
b =0
if b>0:
    print("양수")
elif b==0:
    print("0")
else:
    print("음수")

#example
order = 'spagetti'
price = 0

if order =="spam":
    price = 1000
elif order =="milk":
    price = 500
elif order == "egg":
    price = 100
else:
    price = "없는 상품입니다"

print(f'가격 : {price}')

















