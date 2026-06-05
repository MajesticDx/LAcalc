import array

class Vector:
    def __init__(self, values: array.array):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same size for addition.")
        result_values = array.array('d', (self.values[i] + other.values[i] for i in range(len(self))))
        return Vector(result_values)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same size for subtraction.")
        result_values = array.array('d', (self.values[i] - other.values[i] for i in range(len(self))))
        return Vector(result_values)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.scalar_multiplication(other)
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same size for multiplication.")
        result_values = array.array('d', (self.values[i] * other.values[i] for i in range(len(self))))
        return Vector(result_values)

    def __rmul__(self, scalar):
        return self.scalar_multiplication(scalar)

    def scalar_multiplication(self, scalar):
        result_values = array.array('d', (self.values[i] * scalar for i in range(len(self))))
        return Vector(result_values)

    def scalar_product(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same size for scalar product.")
        return sum(self.values[i] * other.values[i] for i in range(len(self)))

    def norm(self):
        return sum(x ** 2 for x in self.values) ** 0.5

    def normalize(self):
        norm_value = self.norm()
        if norm_value == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self.scalar_multiplication(1 / norm_value)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        if len(self) != len(other):
            return False
        return all(self.values[i] == other.values[i] for i in range(len(self)))

    def __repr__(self):
        return f"Vector({list(self.values)})"

    def __str__(self):
        return f"Vector({list(self.values)})"