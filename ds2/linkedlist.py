# my_list = list(range(1,10))
# my_list.remove(6)
# print(my_list)


# custom linked list

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add(self,new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

link = Linked()   
elem = Node('Edureka')  
link.head = elem  
elem2 = Node('Python') 
link.head.next = elem2     
link.show()  
link.add("certification")
link.show()