
class Queue:
    def __init__(self):
        self.queue = []
        pass

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.queue.insert(0, item)
        
    def dequeue(self):
        return self.queue.pop()
        
    def size(self):
        return len(self.queue)
        
    def peek(self):
        return len