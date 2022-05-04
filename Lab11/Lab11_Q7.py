
class CircularQueue:

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.max_queue = capacity
        self.front = 0
        self.back = self.max_queue - 1
        self.count = 0

    def enqueue(self, item):
        if not self.is_full():
            self.back = (self.back + 1) % self.max_queue
            self.items[self.back] = item
            self.count += 1


    def dequeue(self):
        if not self.is_empty():
            item = self.items[self.front]
            self.front = (self.front + 1) % self.max_queue
            self.count -= 1
            return item

    def is_full(self):
        return self.count == self.max_queue

    def is_empty(self):
        return self.count == 0

    def peek(self):
        return self.items[self.front]

    def __str__(self):
        output_str = "-> |"
        if self.back < self.front:
            for index in range(self.front, self.max_queue):
                if index == (self.back):
                    output_str += str(self.items[index])
                else:
                    output_str += str(self.items[index]) + ", "
            for index in range(0, self.back+1):
                if index == (self.back):
                    output_str += str(self.items[index])
                else:
                    output_str += str(self.items[index]) + ", "
        else:
            if (self.count == 0):
                output_str += "| ->"
                return output_str
            else:
                for index in range(self.front, self.back+1):
                    if index == (self.back):
                        output_str += str(self.items[index])
                    else:
                        output_str += str(self.items[index]) + ", "
        output_str += "| ->"
        return output_str
        
"""
ENQUE

"""
 	

q = CircularQueue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
print(q)
q.dequeue()
q.dequeue()
print(q)


"""
q = CircularQueue(7)
q.enqueue("abc")
q.enqueue("def")
q.dequeue()
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.dequeue()
q.enqueue("hello")
q.enqueue("world")
q.enqueue("zach")
q.enqueue(30)
print(q)
"""
"""
[None, "def", None, None, None, None, "abc"]
front = 1
back = 1
count = 2


"""