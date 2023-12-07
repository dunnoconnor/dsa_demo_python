class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.size() < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)