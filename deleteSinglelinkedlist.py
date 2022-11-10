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
        new_node.next = self.head
        self.head = new_node
    #delete 1st occurrence ofkeyin linkedlist
    def deleteNode(self, key):
        temp = self.head

        #if head node has the node to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        #search for the key to be deleted
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        #if key is not in the list
        if temp == None:
            return

        #unlink node from linkedlist
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(" %d" % (temp.data)),
            temp = temp.next

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
  
print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()