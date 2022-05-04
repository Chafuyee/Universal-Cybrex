def br():
    print("=" * 20)

br()

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
        new_node = Node(new_object, self.next)
        self.set_next(new_node)
    
    def remove_after(self):
        remove_node = self.get_next()
        new_link = remove_node.get_next()
        self.set_next(new_link)

node1 = Node('10')
node2 = Node('20')
node3 = Node('30')
node4 = Node('40')
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1.get_next().get_next().get_data())
print(node1.get_next().get_next().get_next().get_data())
print()
node2.remove_after()
print(node1.get_data())
print(node1.get_next().get_data())
print(node1.get_next().get_next().get_data())

br()