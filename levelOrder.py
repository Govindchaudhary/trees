import collections

class Node(object):
    def __init__(self,key):
         self.leftChild = None
         self.rightChild = None
         self.key = key

def levelOrder(root):
    if root is None:
        return
    nodes = collections.deque([root])
    #Current level count indicates how many nodes should be printed at this level
    # before printing a new line
    #Next level count contains the number of nodes in the next level, 
    #which will become the current level count after printing a new line
    currentCount,nextCount = 1,0
    while len(nodes):
        currentNode = nodes.popleft()
        print currentNode.key,
        currentCount-=1

        #We count the number of nodes in the next level by
        # counting the number of children of the nodes in the current level
        if currentNode.leftChild:
             nodes.append(currentNode.leftChild)
             nextCount+=1
        if currentNode.rightChild:
            nodes.append(currentNode.rightChild)
            nextCount+=1
        
        if currentCount==0:
            print '\n'
            currentCount,nextCount = nextCount,currentCount

root = Node(1)
root.leftChild=Node(2)
root.rightChild=Node(3)
root.leftChild.leftChild=Node(4)
root.leftChild.rightChild=Node(5)
root.rightChild.leftChild= Node(6)
root.rightChild.rightChild= Node(7)

levelOrder(root)

    