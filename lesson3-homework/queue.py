class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f'{item} added to the Q')

    def dequeue(self):
        if len(self.items) < 1:
            print('Q is empty!')
            return None
        else:
            return self.items.pop(0)

    def get_first(self):
        return self.items[0]
        pass

    def get_last(self):
        return self.items[-1]
        pass

    def size(self):
        return len(self.items)

    def is_empty(self):
        return False if self.size() > 0 else True


q = Queue()

print(f'Q is empty: {q.is_empty()}')

q.enqueue('first_in')
q.enqueue('second_in')
q.enqueue('third_in')

print(f'All items in the Q: {q.items}')

print(q.get_first())
print(q.get_last())

print(f'First out: {q.dequeue()}')
