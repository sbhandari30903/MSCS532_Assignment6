class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # inserts value at a specific row and column.
    def insert(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column out of range")
        self.matrix[row][col] = value

    # deletes value at a specific row and column (set to 0)
    def delete(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column out of range")
        self.matrix[row][col] = 0

    # access value at a specific row and column
    def access(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column out of range")
        return self.matrix[row][col]

    # string representation of the matrix
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

# Example usage:
matrix = Matrix(3, 3)
matrix.insert(0, 0, 1)
matrix.insert(1, 1, 2)
matrix.insert(2, 2, 3)
print(matrix)
# Output:
# 1 0 0
# 0 2 0
# 0 0 3

matrix.delete(1, 1)
print(matrix)
# Output:
# 1 0 0
# 0 0 0
# 0 0 3

print(matrix.access(2, 2))  # Output: 3