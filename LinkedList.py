'''
Author: Sai Uday Bhaskar Mudivarty
Program: Single Linked List
'''

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self,data):
        newNode = Node(data,None)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
        self.size = self.size + 1
    
    def delete(self,data):
        isFound = False
        currentNode = self.root
        while not isFound and currentNode != None:
            if currentNode.data == data:
                if currentNode == self.root:
                    self.root = currentNode.next
                else:
                    prev.next = currentNode.next
                del currentNode
                self.size = self.size -1
                isFound = True
                print ("Deleted "+str(data)+" from the linked list")
                break
                
            prev = currentNode
            currentNode = currentNode.next
        if not isFound:
            raise ValueError("Value not found in LinkedList")
        
    
    def printList(self):
        currentNode = self.root
        i = 1
        while currentNode != None:
            print(str(i)+ ". "+str(currentNode.data))
            currentNode = currentNode.next
            i+=1
    
    def search(self,data):
        currentNode = self.root
        while currentNode !=None:
            if currentNode.data == data:
                print("Found "+str(data)+" in the linked list")
                return currentNode
            currentNode = currentNode.next
        print(str(data)+" is not found in the linked list")
    
    def addAsRoot(self,data):
        newNode = Node(data,self.root)
        self.root = newNode
    
    def addAtNthPosition(self,data,n):
        try:        
            if n ==1:
                self.addAsRoot(data)
            elif n > self.__len__()+1:
                raise StandardError()
            else:
                
                currentNode = self.root
                for i in range(1,n-1):
                    currentNode = currentNode.next
                newNode = Node(data,currentNode.next)
                currentNode.next = newNode
                
        except StandardError:
            print("The size of the linked list is less than the size of the desired position")
            print("Unable to Add "+str(data)+ " at "+str(n)+" position.")
        
    def __len__(self):
        return self.size
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(12)
    ll.add(14)
    ll.add(100)
    ll.printList()
    print("")
    ll.addAtNthPosition(101,5)
    ll.printList()
    ll.addAsRoot(1)
    print("")
    ll.printList()
    ll.search(14)
    ll.delete(14)
    ll.search(14)




            
        

                    


