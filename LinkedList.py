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
        self.printList()
        while not isFound and currentNode != None:
            if currentNode.data == data:
                if currentNode == self.root:
                    self.root = currentNode.next
                else:
                    prev.next = currentNode.next
                del currentNode
                self.size = self.size -1
                isFound = True
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
    
    def __len__(self):
        return self.size
    

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(12)
    ll.delete(14)
    print(len(ll))



            
        

                    


