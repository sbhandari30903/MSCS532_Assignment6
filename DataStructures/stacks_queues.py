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
        # Initialize an empty list to store queue elements
        self.items = []
    
    def enqueue(self, item):
        # Add an item to the end of the queue
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
