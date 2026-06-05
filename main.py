from src.Matrix import Matrix
from src.Vector import Vector

a = Vector([1.0, 2.0, 3.0])
b = Vector([4.0, 5.0, 6.0])
c = Vector([1.0, 2.0])
d = Vector([3.0, 4.0])
x = Matrix([a, b])
z = Matrix([c, d])

print(z @ x)
print(x.transpose())