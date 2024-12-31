"""
One of the best part of coding is to revisit old code and refactor it. 
"""
class Node: 
    next = None
    
    def __init__(self, data):
        self._data = data;
        
    def display(self):
        print("Node has value", self._data)


node_obj_a = Node(4)
node_obj_b = Node(5)
node_obj_c = Node(6)

node_obj_a.next = node_obj_b
node_obj_b.next = node_obj_c

node = node_obj_a

while(node is not None):
    node.display()
    node = node.next 
