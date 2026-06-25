import array
from .Vector import Vector

class Matrix:
    def __init__(self, rows: list):
        if not isinstance(rows, list) or len(rows) == 0:
            raise ValueError("Matrix should be of list type and not empty")

        self.rows = [row if isinstance(row, Vector) else Vector(array.array('d', row)) for row in rows]

        row_len = len(self.rows[0])
        for vector in self.rows:
            if len(vector) != row_len:
                raise ValueError("All rows must have the same length")

    @property
    def shape(self):
        return len(self.rows), len(self.rows[0])

    def __getitem__(self, index):
        return self.rows[index]

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape for addition.")
        result_rows = [self.rows[i] + other.rows[i] for i in range(len(self.rows))]
        return Matrix(result_rows)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape for subtraction.")
        result_rows = [self.rows[i] - other.rows[i] for i in range(len(self.rows))]
        return Matrix(result_rows)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Matrix can only be multiplied by a scalar.")
        result_rows = [row * other for row in self.rows]

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Number of 1. Matrix columns must equal the number of 2. Matrix rows for multiplication.")
        result_rows = []
        for v in range(self.shape[0]):
            result_values = array.array('d')
            for i in range(other.shape[1]):
                result_value = sum(self.rows[v][k] * other.rows[k][i] for k in range(self.shape[1]))
                result_values.append(result_value)
            result_rows.append(Vector(result_values))
        return Matrix(result_rows)

    def transpose(self):
        transposed_rows = []
        for i in range(self.shape[1]):
            transposed_values = array.array('d', (self.rows[j][i] for j in range(self.shape[0])))
            transposed_rows.append(Vector(transposed_values))
        return Matrix(transposed_rows)

    def is_square(self):
        return self.shape[0] == self.shape[1]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.shape != other.shape:
            return False
        return all(self.rows[i] == other.rows[i] for i in range(len(self.rows)))

    def __repr__(self):
        return f"Matrix({self.rows})"

    def __str__(self):
        return "\n".join([str(row) for row in self.rows])

    def trace(self):
        if not self.is_square():
            raise ValueError("Spur can only be calculated for square matrices.")
        return sum(self.rows[i][i] for i in range(self.shape[0]))

    # with laplace expansion
    def determinant(self):
        if not self.is_square():
            raise ValueError("Determinant can only be calculated for square matrices.")
        if self.shape[0] == 1:
            return self.rows[0][0]
        if self.shape[0] == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        det = 0
        for row_index in range(self.shape[0]):
            multiplicant = ((-1) ** row_index) * self.rows[row_index][0]
            sub_matrix = self.create_sub_matrix(0, row_index)
            det += multiplicant * sub_matrix.determinant()

        return det

    # creates a matrix with a column and row cut out
    def create_sub_matrix(self, column, row):
        sub_matrix_rows = []
        for i in range(self.shape[0]):
            if i == row:
                continue
            sub_row_values = array.array('d', (self.rows[i][j] for j in range(self.shape[1]) if j != column))
            sub_matrix_rows.append(Vector(sub_row_values))
        return Matrix(sub_matrix_rows)


