# test (HW)

try:
    from point import Point
    from add import Add
    from multiply import Multiply
except ImportError as e:
    print(e)

p1 = Point(10, 20)
print(p1)

p2 = Point()
print(p2)

p2.set_x(100)
print(p2)

# Test for Add
a = Add(10, 20)
z = a.forward(10, 20)
print(z)

# Test for Multifly
m = Multiply()
out = m.forward(10, 20)
print(out)      # 200
print(m)        # 'multiply (x=10, y=20)'

