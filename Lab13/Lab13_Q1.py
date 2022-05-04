
class Node:
    
    def __init__(self, data, after = None):
        self.data = data
        self.next = after

    def __str__(self):
        return self.get_data()
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, new_object):
        new_node = Node(new_object, self.get_next)
        self.set_next(new_node)
