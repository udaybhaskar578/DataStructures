'''
Author: Sai Uday Bhaskar Mudivarty
Program: Binary search tree
'''

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, data):
        self.data = data

    @property
    def left(self):
        return self.left

    @left.setter
    def left(self, left):
        self.left = left

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0

    @property
    def root(self):
        return self.root
    @root.setter
    def root(self, root):
        self.root = root

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.height = height
    
    def Insert(self,root,data):
        if root == None:
            root = Node(data)
        elif data <= root.data:
            root.left = Insert(root.left,data)
        else:
            root.right = Insert(root.right,data)
        return root
    
    def Search(self,root,data):
        if root == None:
            return False
        elif data == root.data:
            return True
        elif data <= root.data:
            Search(root.left,data)
        else:
            Search(root.right,data)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.root == bst.Insert(bst.root,15)
    print("After Initialization"+bst.root)
    bst.root == bst.Insert(bst.root,12)
    bst.root == bst.Insert(bst.root,10)
    bst.root == bst.Insert(bst.root,18)
    bst.root == bst.Insert(bst.root,19)
    bst.root == bst.Insert(bst.root,25)
    bst.root == bst.Insert(bst.root,21)
    bst.root == bst.Insert(bst.root,17)


    print(bst.Search(bst.root,16))
    print(bst.Search(bst.root,17))

