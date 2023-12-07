from stack import Stack
def test_stack():
    stack = Stack()

    # Test push
    stack.push("A")
    assert stack.size() == 1

    # Test pop
    stack.push("B")
    assert stack.pop() == "B"
    assert stack.pop() == "A"

    # Test pop on empty stack
    assert stack.pop() is None

    # Test pop on empty stack after pushing and popping elements
    stack.push("A")
    stack.push("B")
    stack.pop()
    stack.pop()
    assert stack.pop() is None

test_stack()