class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert new value - 0(1)
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)
    
    # Search list for a value - 0(n)
    def contains(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    # Add remove method which locates a specific data value and removes it - 0(n)
    def remove(self, data):
        if not self.head:
            return
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next
    
    # reverse list - 0(n)
    def reverse(self):
        node = self.head
        previous = None
        while node:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        self.head = previous