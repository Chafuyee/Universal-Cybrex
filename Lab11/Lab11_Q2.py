
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

    def clear(self):
        for index in range(len(self.queue)):
            self.queue.pop()

    def __str__(self):
        output_str = "-> |"
        for index in range(len(self.queue)):
            if index == (len(self.queue)-1):
                output_str += str(self.queue[index])
            else:
                output_str += str(self.queue[index]) + ", "
        output_str += "| ->"
        return output_str