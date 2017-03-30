'''
Author: Sai Uday Bhaskar Mudivarty
Program: Double Linked List
'''
class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def insertAtNthPosition(self,data,n):
        try:        
            if n ==1:
                self.insertAtHead(data)
            elif n > self.__len__()+1:
                raise StandardError()
            else:
                currentNode = self.root
                for i in range(1,n-1):
                    currentNode = currentNode.next
                newNode = Node(data,currentNode.next,currentNode)
                currentNode.next = newNode
                self.size = self.size +1
        except StandardError:
            print("The size of the linked list is less than the size of the desired position")
            print("Unable to Add "+str(data)+ " at "+str(n)+" position.")
    def insertAtHead(self,data):
        newNode = Node(data,None,None)
        if self.root == None:
            self.root = newNode
        else:
            newNode.next = self.root
            self.root.prev = newNode
            self.root = newNode
        self.size = self.size + 1
    def insertAtEnd(self,data):
        newNode = Node(data,None,None)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
        self.size = self.size + 1

    def printList(self):
        if self.root != None:
            currentNode = self.root
            i = 1
            print("Printing list in a forward order:")
            while currentNode != None:
                print(str(i)+". "+str(currentNode.data))
                currentNode = currentNode.next
                i=i+1
        else:
            print("No elements are available in the list")


    def reversePrint(self):
        if self.root != None:
            currentNode = self.root
            i = 1
            print("Printing list in a reverse order:")
            while currentNode.next != None:
                currentNode = currentNode.next
            while currentNode !=None:
                print(str(i)+". "+str(currentNode.data))
                currentNode = currentNode.prev
        else:
            print("No elements are available in the list")

    def search(self,data):
        currentNode = self.root
        while currentNode !=None:
            if currentNode.data == data:
                print("Found "+str(data)+" in the linked list")
                return currentNode
            currentNode = currentNode.next
        print(str(data)+" is not found in the linked list")

    def delete(self,data):
        isFound = False
        currentNode = self.root
        while not isFound and currentNode != None:
            if currentNode.data == data:
                if currentNode == self.root:
                    self.root = currentNode.next
                    self.root.prev = None
                else:
                    latterNode = currentNode.next
                    latterNode.prev = prev
                    prev.next = latterNode
                del currentNode
                self.size = self.size -1
                isFound = True
                print ("Deleted "+str(data)+" from the linked list")
                break
            prev = currentNode
            currentNode = currentNode.next
        if not isFound:
            raise ValueError("Value not found in LinkedList")

    def deleteNodeAtNthPosition(self,n):
        try:
            currentNode = self.root
            if n == 1:
                self.root = currentNode.next
                del currentNode
            elif n > self.__len__()+1:
                raise StandardError()
            else:
                for i in range(1,n-1):
                    currentNode = currentNode.next
                
                latterNode = (currentNode.next).next
                latterNode.prev = currentNode
                currentNode.next = latterNode 
                x = currentNode.next
                del x
                
        except StandardError:
            print("Out Of Bound: Unable to delete the element at "+str(n)+" position")\

    def __len__(self):
        return self.size
    
                
if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insertAtEnd(10)
    ll.insertAtEnd(12)
    ll.insertAtEnd(14)
    ll.insertAtEnd(100)
    ll.printList()
    print("")
    ll.delete(12)

    ll.insertAtEnd(101)
    ll.insertAtEnd(102)
    ll.printList()
    print("")
    ll.deleteNodeAtNthPosition(3)
    ll.printList()

