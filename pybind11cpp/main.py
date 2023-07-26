from pybind11_demo import *

a = 11
b = 22
print(a, "+", b, "= ", add(a, b))

a = 1.11
b = 2.22

print(a, "+", b, "= ", add(a, b))

a = "Hello"
b = "World"
print(a, "+", b, "= ", add(a, b))

b = Bird("ABC")
print(b.name())
b.fly()