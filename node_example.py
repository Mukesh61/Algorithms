
class node: 
    next = None
    def __init__(self,data):
        self.data=data;
        
    def display(self):
        print("node has value",self.data)


a=node(4)
b=node(5)
c=node(6)
a.next=b
b.next=c
node=a
while(node is not None):
    node.display()
    node=node.next
    
