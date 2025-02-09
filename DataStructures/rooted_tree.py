from linked_list import SinglyLinkedList

class TreeNode:
    def __init__(self, data):
        # Initialize a tree node with data and a linked list of children
        self.data = data
        self.children = SinglyLinkedList()

    def add_child(self, child):
        # Add a child node to the linked list of children
        self.children.insert_at_end(child)

    def remove_child(self, key):
        # Remove a child node with the given key from the linked list
        self.children.delete_node(key)

    def traverse(self):
        # Perform a depth-first traversal and print nodes
        print(self.data, end=" -> ")
        temp = self.children.head
        while temp:
            temp.data.traverse()
            temp = temp.next

# Example usage of Rooted Tree
root = TreeNode("A")  # Root node
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

root.traverse()  # Output: A -> B -> D -> C ->
