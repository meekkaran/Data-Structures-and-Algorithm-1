class Node:
    #a function to initialise a node
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    #initialise head of the linkedList
    def __init__(self):
        self.head = None
        
    #add a node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head #point the next of new node to the head
        self.head = new_node
        
    #add a node after a given node
    def insertAfter(self, prev_node, new_data):
        #check if prev node exists
        if prev_node is None:
            print("the given node is linkedlist")
            return
        #allocate new node, assign data to it
        new_node = Node(new_data)
        new_node.next = prev_node.next #make next of new node be the next of prev node
        prev_node.next = new_node
        
    #add a node at the end
    def append(self, new_data):
        #check if its empty, then make new node the head
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        #else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node #change the pointer of last node to point to the next
    
    #function to print linked list
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()
    
    llist.append(9)
    llist.push(10)
    llist.push(6)
    llist.append(7)
    llist.insertAfter(llist.head.next, 8)
    
    print('created linkedlist is  ')
    llist.printlist()
    
        