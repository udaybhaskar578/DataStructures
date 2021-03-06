'''
Author: Sai Uday Bhaskar Mudivarty
Program: Binary search tree
'''
import Queue
import sys



class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._Insert(self.root,data)

    def _Insert(self,node,data):
        if data <= node.data:
            if node.left ==None:
                node.left = Node(data)
            else:
                self._Insert(node.left,data)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self._Insert(node.right,data)

    def Search(self,root,data):
        if root == None:
            return False
        elif data == root.data:
            return True
        elif data <= root.data:
            return self.Search(root.left,data)
        else:
            return self.Search(root.right,data)
        
    def _FindMin(self,root):
        if root == None:
            return -1
        elif root.left == None:
            return root.data
        return self._FindMin(root.left)
    
    def FindMin(self):
        if self.root == None:
            return -1
        else:
            return self._FindMin(self.root)

    def _FindMax(self,root):
        if root == None:
            return -1
        elif root.right == None:
            return root.data
        return self._FindMax(root.right)
    
    def FindMax(self):
        if self.root == None:
            return -1
        else:
            return self._FindMax(self.root)
            
    def _HeightOfTree(self,root):
        if root == None:
            return -1
        left = self._HeightOfTree(root.left)
        right = self._HeightOfTree(root.right)

        return max(left,right)+1

    def HeightOfTree(self):
        if self.root == None:
            return -1
        else:
            return self._HeightOfTree(self.root)

    def LevelOrderTraversal(self):
        print("Level Order Traversal: Breadth First Search")
        if self.root == None:
            return
        q = Queue.Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            currentNode = q.front()
            print(currentNode.data)
            if currentNode.left !=None:
                q.enqueue(currentNode.left)
            if currentNode.right !=None:
                q.enqueue(currentNode.right)
            q.dequeue()

    def PreOrderTraversal(self):
        if self.root == None:
            return
        else:
            print("Depth First Preorder Traversal <Root><Left><Right>")
            self._PreOrderTraversal(self.root)
            print()
    
    def _PreOrderTraversal(self,node):
        if node == None:
            return
        print(node.data,end=",")
        self._PreOrderTraversal(node.left)
        self._PreOrderTraversal(node.right)

    def InOrderTraversal(self):
        if self.root == None:
            return
        else:
            print("Depth First Inorder Traversal: Gives you elements in a sorted order <Left><Root><Right>")
            self._InOrderTraversal(self.root)
            print()
    
    def _InOrderTraversal(self,node):
        if node == None:
            return
        self._InOrderTraversal(node.left)
        print(node.data,end=",")
        self._InOrderTraversal(node.right)

    def PostOrderTraversal(self):
        if self.root == None:
            return
        else:
            print("Depth First Postorder Traversal:<Left><Right><Root>")
            self._PostOrderTraversal(self.root)
            print()
    
    def _PostOrderTraversal(self,node):
        if node == None:
            return
        self._PostOrderTraversal(node.left)
        self._PostOrderTraversal(node.right)
        print(node.data,end=",")
    
    def IsBSTCheck(self):
        return self._IsBSTCheckUtil(self.root,-sys.maxsize,sys.maxsize)
    
    def _IsBSTCheckUtil(self,node,min,max):
        if node == None:
            return True
        if ((node.data >= min) and (node.data < max) and 
        (self._IsBSTCheckUtil(node.left,min,node.data)) and 
        (self._IsBSTCheckUtil(node.right,node.data,max))):
            return True
        else:
            return False


        
            
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.Insert(15)
    # print("After Initialization"+str(bst.root.data))
    bst.Insert(12)
    # print("After Initialization"+str(bst.root.left.data))
    bst.Insert(10)
    # print("After Initialization"+str((bst.root.left).left.data))
    bst.Insert(19)
    bst.Insert(25)
    bst.Insert(21)
    bst.Insert(17)    
    print(bst.Search(bst.root,22))
    print(bst.FindMax())
    print(bst.FindMin())
    print(bst.HeightOfTree())
    bst.LevelOrderTraversal()
    bst.PreOrderTraversal()
    bst.InOrderTraversal()
    bst.PostOrderTraversal()
    print(bst.IsBSTCheck())