from linked_list import LinkedList
# Initialize a linked list
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
assert linked_list.contains(1) == True
assert linked_list.contains(2) == True
print("initialization passed")

# Remove a node from the linked list
linked_list.remove(1)
assert linked_list.contains(1) == False
assert linked_list.contains(2) == True
linked_list.remove(2)
assert linked_list.contains(2) == False
print("remove method tests passed")

# Ensure that nodes are correctly linked
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
assert linked_list.head.data == 1
assert linked_list.head.next.data == 2
assert linked_list.head.next.next.data == 3
print("node tests passed")

# Reverse the linked list
linked_list.reverse()
# Ensure the list is now reversed
assert linked_list.head.data == 3
assert linked_list.head.next.data == 2
assert linked_list.head.next.next.data == 1
print("reverse methods passed")