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
    print root.key
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

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 90)
inorder(root)
root = deleteNode(root,20)
print 'root after deletion is:'
print root.key
print 'after deletion:'
inorder(root)



             
