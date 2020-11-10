a = 20
b = 20+10

print(a, type(a))
print(a, isinstance(b, int))


#2진수
c=0b1101
print(c)

d = 0o23
print(d)

e=0x23
print(e)


#승
f = 2**1024
print(f, type(f))

print(f.bit_length())

#변환
print(oct(38))
print(hex(38))
print(bin(38))