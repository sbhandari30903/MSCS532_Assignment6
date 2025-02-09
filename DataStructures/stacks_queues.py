class Stack:
    def __init__(self):
        # initialize an empty list
        self.items = []
    
    def push(self, item):
        # add an item to the top of the stack
        self.items.append(item)
    
    def pop(self):
        # remove and return the top item from the stack, if not empty
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        # returns the top item of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        # check if the stack is empty
        return len(self.items) == 0
    
    def size(self):
        # returns the number of items in the stack
        return len(self.items)


class Queue:
    def __init__(self):
        # initialize an empty list
        self.items = []
    
    def enqueue(self, item):
        # add an item to the end of the queue
        self.items.append(item)
    
    def dequeue(self):
        # remove and return the front item from the queue, if not empty
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        # return the front item of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        # checks if the queue is empty
        return len(self.items) == 0
    
    def size(self):
        # return the number of items in the queue
        return len(self.items)


# stack example
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False
print(stack.size())  # Output: 2

# Queue example
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.is_empty())  # Output: False
print(queue.size())  # Output: 2