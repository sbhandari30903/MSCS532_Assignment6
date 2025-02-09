
class Array:
    def __init__(self):
        self.array = []

    # insert a value at a specific index
    def insert(self, index, elem):
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of range")
        self.array.insert(index, elem)

    # deletes the value from a specific index
    def delete(self, index):
        if index < 0 or index >= len(self.array):
             raise IndexError("Index out of range")
        return self.array.pop(index) 

    # returns element from the specific index
    def access(self, index):
        if index < 0 or index >= len(self.array):
             raise IndexError("Index out of range")
        return self.array[index]
    
    # string representation of the array.
    def __str__(self):
        return str(self.array)
    
# Example usage:
arr = Array()
print(arr)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
print(arr)  # Output: [10, 20, 30]

arr.delete(1)
print(arr)  # Output: [10, 30]

print(arr.access(0))  # Output: 10