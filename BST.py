def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue = enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)    

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found") 
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found") 
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found") 
        else:
            searchNode(rootNode.rightChild, nodeValue)

newBST = BSTNode(None)
insertNode(newBST ,70)
insertNode(newBST ,50)
insertNode(newBST ,90)
insertNode(newBST ,30)
insertNode(newBST ,60)
insertNode(newBST ,80)
insertNode(newBST ,100)
insertNode(newBST ,20)
insertNode(newBST ,40)
levelOrderTraversal(newBST)
searchNode(newBST, 60)