from collections import deque

class MyStack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return False if self.size() > 0 else True

    def push(self, item):
        self.items.append(item)
        print('Item is appended at the top of the Stack')

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty!')
            return None

    def top(self):
        return self.items[-1]

    def bottom(self):
        return self.items[0]

    def size(self):
        return len(self.items)


s = MyStack()

s.push('first_in')
s.push('second_in')
s.push('third_in')

print(f'All items in the Stack: {(s.items)}')

print(s.bottom())
print(s.top())
print(f'First out: {s.pop()}')
