class BinaryHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def precUp(self,i):   # restore the heap pty if destroyed by new item at index i
                          # by moving the key at given index to all the way up reqd to restore the heap
        while i//2 >0:
           if self.heapList[i] < self.heapList[i//2]:
               temp = self.heapList[i]
               self.heapList[i] = self.heapList[i//2]
               self.heapList[i//2] = temp
           i =i//2
    
    def insert(self,key):
        self.heapList.append(key)
        self.currentSize+=1
        self.precUp(self.currentSize)

    def delMin(self):
        minElement = self.heapList[1]
        self.heapList[1]= self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.precDown(1)  # restore the structure of heap destroyed by this new root
                          
        return minElement
    
    def precDown(self,i):  # take the value at this index and move down this value to its correct position to maintain the heap pty
        while 2*i <=self.currentSize:
            mc = self.minChild(i)  # index of minchild of node at index i
            if self.heapList[i] > self.heapList[mc] :
                 temp = self.heapList[i]
                 self.heapList[i] = self.heapList[mc]
                 self.heapList[mc] = temp
            i=mc

    def minChild(self,i):
        if 2*i+1 > self.currentSize:   # child of node index at i are at 2*i and 2*i+1
           return 2*i
        else:
          if self.heapList[2*i] > self.heapList[2*i+1]:
             return 2*i+1
          else:
              return 2*i

    
    def buildHeap(self,listOfKeys):
         i = len(listOfKeys)//2
         self.heapList = [0] + listOfKeys[:]
         self.currentSize = len(listOfKeys)
         while i>0:    # start from the middle of the list and restores the heap property by moving the element at index all the way to down reqd to restore
            self.precDown(i)
            i=i-1
         return self.heapList
    


myHeap = BinaryHeap()
myHeap.insert(5)
myHeap.insert(9)
myHeap.insert(11)
myHeap.insert(14)
myHeap.insert(18)
myHeap.insert(19)
myHeap.insert(21)
myHeap.insert(33)
myHeap.insert(17)
myHeap.insert(27)
myHeap.insert(7)
print 'heap is:'
print myHeap.heapList
myHeap.delMin()
print 'heap after deleting min:'
print myHeap.heapList
print 'heap from given list of keys:'
print myHeap.buildHeap([9,6,5,2,3])
