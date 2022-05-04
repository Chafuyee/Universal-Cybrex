
def br():
    print("=" * 40)

br()

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
        if len(self.queue) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.queue.pop()
        
    def size(self):
        return len(self.queue)
        
    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.queue[-1]

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

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        if len(self.stack)== 0:
            stack_str = "[ "
        else:
            stack_str = "["
            for index in range(len(self.stack)):
                if isinstance(self.stack[index], str):
                    if index == (self.size()-1):
                        stack_str += "'" + (str(self.stack[index])) + "' "
                    else: 
                        stack_str += "'" + (str(self.stack[index])) + "', "
                else:
                    if index == (self.size()-1):
                        stack_str += (str(self.stack[index])) + " "
                    else: 
                        stack_str += (str(self.stack[index])) + ", "
        stack_str += "<-"
        return stack_str

    def clear(self):

        for index in range(len(self.stack)):
            self.stack.pop()


def merge_queues(q1, q2):
    
    combined_queue = Queue()
    q1_size = q1.size()
    q2_size = q2.size()

    if not q1.is_empty() and q2.is_empty():
        while not q1.is_empty():
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                q1_element = q1.dequeue()
                q2_element = q2.dequeue()
                if q1_element <= q2_element:
                    combined_queue.enqueue(q1_element)
                    combined_queue.enqueue(q2_element)
                elif q1_element >= q2_element:
                    combined_queue.enqueue(q2_element)
                    combined_queue.enqueue(q1_element)
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())

    if q1.is_empty() and not q2.is_empty():
        while not q2.is_empty():
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                q1_element = q1.dequeue()
                q2_element = q2.dequeue()
                if q1_element <= q2_element:
                    combined_queue.enqueue(q1_element)
                    combined_queue.enqueue(q2_element)
                elif q1_element >= q2_element:
                    combined_queue.enqueue(q2_element)
                    combined_queue.enqueue(q1_element) 
                    
    if not q1.is_empty() and not q2.is_empty():
        while not q2.is_empty() and not q1.is_empty():
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                if q2_size < q1_size:
                    q1_element = q1.dequeue()
                    q2_element = q2.dequeue()
                    q1_element2 = q1.dequeue()
                    if q1_element <= q2_element:
                        combined_queue.enqueue(q1_element)
                        combined_queue.enqueue(q2_element)
                        combined_queue.enqueue(q1_element2)
                    elif q1_element >= q2_element:
                        combined_queue.enqueue(q2_element)
                        combined_queue.enqueue(q1_element)
                        combined_queue.enqueue(q1_element2)
                else:
                    q1_element = q1.dequeue()
                    q2_element = q2.dequeue()
                    if q1_element <= q2_element:
                        combined_queue.enqueue(q1_element)
                        combined_queue.enqueue(q2_element)
                    elif q1_element >= q2_element:
                        combined_queue.enqueue(q2_element)
                        combined_queue.enqueue(q1_element)
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())

    

    return combined_queue

queue1 = Queue()
queue2 = Queue()
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(6)
queue2.enqueue(1)
queue2.enqueue(5)
queue2.enqueue(7)
print(merge_queues(queue1, queue2))


br()

"""
def merge_queues(q1, q2):

    combined_queue = Queue()

    if not q1.is_empty() and q2.is_empty():
        while not q1.is_empty():
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                q1_element = q1.dequeue()
                q2_element = q2.dequeue()
                if q1_element <= q2_element:
                    combined_queue.enqueue(q1_element)
                    combined_queue.enqueue(q2_element)
                elif q1_element >= q2_element:
                    combined_queue.enqueue(q2_element)
                    combined_queue.enqueue(q1_element)
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())

    if q1.is_empty() and not q2.is_empty():
        while not q2.is_empty():
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                q1_element = q1.dequeue()
                q2_element = q2.dequeue()
                if q1_element <= q2_element:
                    combined_queue.enqueue(q1_element)
                    combined_queue.enqueue(q2_element)
                elif q1_element >= q2_element:
                    combined_queue.enqueue(q2_element)
                    combined_queue.enqueue(q1_element) 
                    
    if not q1.is_empty() and not q2.is_empty():
        while not q2.is_empty() and not q1.is_empty():
            if (q1.is_empty() == False) and (q2.is_empty() == False):
                q1_element = q1.dequeue()
                q2_element = q2.dequeue()
                if q1_element <= q2_element:
                    combined_queue.enqueue(q1_element)
                    combined_queue.enqueue(q2_element)
                elif q1_element >= q2_element:
                    combined_queue.enqueue(q2_element)
                    combined_queue.enqueue(q1_element)
            if q1.is_empty() and (not q2.is_empty()):
                combined_queue.enqueue(q2.dequeue())
            if q2.is_empty() and (not q1.is_empty()):
                combined_queue.enqueue(q1.dequeue())

    return combined_queue
"""

"""
queue1 = Queue()
queue2 = Queue()
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(6)
queue2.enqueue(1)
queue2.enqueue(5)
queue2.enqueue(7)
print(merge_queues(queue1, queue2))
"""