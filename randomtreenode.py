# Show how to implement a binary tree
# Actually implement a getRandomNode()
import random

class node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    


class binaryTree:
    
    def __init__(self, n):
        # n must be a node
        self.root = n
        self.size = 1
           

    def findR(self, n, nodeToFind, nodeCount):
        print("Entering findR = ", nodeCount)
        if nodeCount == nodeToFind:
            return n, nodeCount
        
        if n.left != None:
            print("checking left")
            possibleN, nodeCount = self.findR(n.left, nodeToFind, nodeCount + 1)
            print("After left count = ", nodeCount)
            if nodeCount == nodeToFind:
                return possibleN, nodeCount
            
        if n.right != None:
            print("checking right")
            possibleN, nodeCount = self.findR(n.right, nodeToFind, nodeCount + 1)
            print("After right count = ", nodeCount)
            if nodeCount == nodeToFind:
                return possibleN, nodeCount
        
        print("At end count = ", nodeCount)
        return n, nodeCount
    
        
    def getRandomNode(self):
        nodeToFind = random.randint(0, self.size-1)
        print("Find node number ", nodeToFind)
        
        n, nodeCount = self.findR(self.root, nodeToFind, 0)
        return n
    
    
root = node(8)
tree = binaryTree(root)

root.left = node(6)
root.right = node(14)
root.left.left = node(3)
root.right.right = node(22)
root.right.right.left = node(18)
tree.size = 6

print("Value at found node: ", tree.getRandomNode().value)
