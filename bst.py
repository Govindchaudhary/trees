class treeNode(object):
    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

def insert(root,key):
    if root is None:
        root = treeNode(key)
    else:
        if key < root.key:
           root.leftChild = insert(root.leftChild,key)
        else:
            root.rightChild = insert(root.rightChild,key)
    return root

def inorder(root):
    if root is None:
       return
    inorder(root.leftChild)
    print root.key,
    inorder(root.rightChild)

def minValueNode(node):
    current = node
    while current.leftChild:
       current = current.leftChild
    return current

def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root 
 
    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.leftChild = deleteNode(root.leftChild, key)
 
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
       
        root.rightChild = deleteNode(root.rightChild, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
         
        # Node with only one child or no child
        if root.leftChild is None :
            temp = root.rightChild 
            root.rightChild = None
            root = temp
            
            return root 
             
        elif root.rightChild is None :
            temp = root.leftChild
            root.leftChild = None 
            root = temp
           
            return root
 
        # Node with two children: Get the inorder successor
        # (smallest in the rightChild subtree)
        temp = minValueNode(root.rightChild)
 
        # Copy the inorder successor's content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.rightChild = deleteNode(root.rightChild , temp.key)
 
    
    return root 

def trimBST(root,minVal,maxVal):
    if root is None:
       return
    root.leftChild = trimBST(root.leftChild,minVal,maxVal)
    root.rightChild = trimBST(root.rightChild,minVal,maxVal)

'''
If current node’s value is between min and max (min<=node<=max)
 then there’s no action need to be taken, so we return the reference to the node itself
'''
    if minVal <= root.key <= maxVal:
         return root

'''
If current node’s value is less than min, then we return the reference to its right subtree, 
and discard the left subtree. Because if a node’s value is less than min, 
then its left children are definitely less than min since this is a binary search tree.
But its right children may or may not be less than min we can’t be sure, 
so we return the reference to it.

'''
    if root.key<minVal:
        return root.rightChild
        
    if root.key>maxVal:
        return root.leftChild

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 13)
inorder(root)
#root = deleteNode(root,6)

#print 'after deletion:'
print 'after trimming:'
trimBST(root,5,13)

inorder(root)



             
