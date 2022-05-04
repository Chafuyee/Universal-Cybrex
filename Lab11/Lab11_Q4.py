
def br():
    print("=" * 20)

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

def reverse_queue(a_queue):
    
    queue_stack = Stack()
    for index in range(a_queue.size()):
        queue_stack.push(a_queue.dequeue())

    for index in range(queue_stack.size()):
        a_queue.enqueue(queue_stack.pop())

def mirror_queue(a_queue):

    queue_stack1 = Stack()
    queue_stack2 = Stack()
    temp_queue = Queue()
    for index in range(a_queue.size()):
        element = a_queue.dequeue()
        queue_stack1.push(element)
        queue_stack2.push(element)

    #reverse_stack 1
    for index in range(queue_stack1.size()):
        temp_queue.enqueue(queue_stack1.pop())
    for index in range(temp_queue.size()):
        queue_stack1.push(temp_queue.dequeue())

    for index in range(queue_stack1.size()):
        a_queue.enqueue(queue_stack1.pop())
    for index in range(queue_stack2.size()):
        a_queue.enqueue(queue_stack2.pop())

q = Queue()
q.enqueue('Front')
q.enqueue('Middle')
q.enqueue('End')
print(q)
reverse_queue(q)
print(q)
br()