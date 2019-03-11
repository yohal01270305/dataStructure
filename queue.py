class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)  # insert item to always index[0]

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def showqueue(self, index):
        return self.items[index]
