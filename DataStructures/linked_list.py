class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with head as None
        self.head = None

    def insert_at_end(self, data):
        # insert a new node at the end of the linked list
        new_node = Node(data)
        # if empty head points to the new data
        if not self.head:
            self.head = new_node
            return
        # loops through the linked list and last next points to new data
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        # delete the first occurrence of a node with the given key
        temp = self.head
        # if its the first element, make head point to its next
        if temp and temp.data == key:
            self.head = temp.next  
            temp = None
            return
        prev = None
        # loops either to the end or until the key is found
        while temp and temp.data != key:
            # keep track of the previous node
            prev = temp  
            temp = temp.next
        # Key not found
        if not temp:
            return  
        # unlink the node from the list
        prev.next = temp.next  
        temp = None

    def traverse(self):
        # traverse and print the linked list
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# example 
linked_list = SinglyLinkedList()
linked_list.insert_at_end(1)  # Insert 1 
linked_list.insert_at_end(2)  # Insert 2
linked_list.insert_at_end(3)  # Insert 3 
linked_list.traverse()  # Output: 1 -> 2 -> 3 -> None
linked_list.delete_node(2)  # Delete node with value 2
linked_list.traverse()  # Output: 1 -> 3 -> None
