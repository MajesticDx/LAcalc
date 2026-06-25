from src.Matrix import Matrix
from src.Vector import Vector

matrix1_rows = [
    [2, 3, 1, 5, 2],
    [3, 1, 4, 2, 1],
    [1, 5, 2, 3, 4],
    [4, 2, 3, 1, 5],
    [5, 4, 1, 2, 3]
]
matrix1 = Matrix(matrix1_rows)

print(matrix1.determinant())
print(matrix1.spur())