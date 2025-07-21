class Memory:
    def __init__(self):
        self.memory_store = []

    def remember(self, item):
        self.memory_store.append(item)

    def recall(self):
        return self.memory_store
