class BinaryTree(object):
     def __init__(self,rootObj):
          self.key = rootObj
          self.leftChild = None
          self.rightChild = None
      
     def insertLeft(self,newNode):
          if self.leftChild ==None:
              self.leftChild = BinaryTree(newNode)
          else:
              t = BinaryTree(newNode)
              t.leftChild = self.leftChild
              self.leftChild = t 
    
     def insertRight(self,newNode):
          if self.rightChild ==None:
              self.rightChild = BinaryTree(newNode)
          else:
              t = BinaryTree(newNode)
              t.rightChild = self.rightChild
              self.rightChild = t

     def getLeftChild(self):
         return self.leftChild
     def getRightChild(self):
         return self.rightChild

     

     def getRootVal(self):
         return self.key



def inorder(tree):
    if tree==None:
       return
    inorder(tree.getLeftChild())
    print tree.getRootVal()
    inorder(tree.getRightChild())

def preorder(tree):
    if tree==None:
       return
    print tree.getRootVal()
    inorder(tree.getLeftChild())
    
    inorder(tree.getRightChild())

def postorder(tree):
    if tree==None:
       return
    
    inorder(tree.getLeftChild())
    inorder(tree.getRightChild())
    print tree.getRootVal()


mytree = BinaryTree('+')
mytree.insertLeft('a')
mytree.insertRight('b')

#print mytree.getRootVal() 
#print mytree.getLeftChild().getRootVal()
print 'inorder traversal is:'
inorder(mytree)

print 'preorder traversal is:'
preorder(mytree)

print 'postorder traversal is:'
postorder(mytree)
    

