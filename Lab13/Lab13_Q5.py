
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
    
    def get_word_score(self):
        count = 0
        alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for letter in self.data:
            value = alpha_list.index(letter)
            count += value
        return count

    def reverse(self):
        node_str = self.data
        node_str = node_str[-1::-1]
        self.set_data(node_str)

node1 = Node('life')
node2 = Node('is', node1)
node3 = Node('long', node2)
node4 = Node('journey', node3)
node1.reverse()
node4.reverse()
print(node1)
print(node4)
