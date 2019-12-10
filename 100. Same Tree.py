# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

# Success:

# Runtime: 20 ms, faster than 99.11% of Python3 online submissions for Same Tree.
# Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Same Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def createTreeList(tree):
            arr = []
            
            # this would normally be a real queue, not a list
            queue = []
            queue.append(tree)
            
            current = queue.pop(0)
            
            while current:
    
                arr.append(current.val)
                #note 1 ^

                if current.left:
                    queue.append(current.left)
                    arr.append(current.left.val)
                else:
                    arr.append(None)
                    
                if current.right:
                    queue.append(current.right)
                    arr.append(current.right.val)
                else:
                    arr.append(None)
                    
                try:
                    current = queue.pop(0)
                except:
                    current = None
            return arr

        p_list = createTreeList(p)
        q_list = createTreeList(q)    

        return p_list == q_list

# Explanation:

# Basically this is just a Breadth First Search onto a tree to see if they're equal via lists
# the function createTreeList is pretty straight forward, it returns a list to represent the tree in BFS manner.
# you make use of a list to store the list representation of a tree.
# you make use of another list to store the queue you would need to go through each node in the tree.
# we make a varibale called current to name what node we're on.
# in the while, we first make send the current.val to the arr list. 
# we check for both proper left and right nodes. If there's a proper node there we add it to the queue, and send its value to the arr list
# if there isnt a proper left or right just send none to the array to accunt for the blank lefts/rights
# in the try and catch we try to assign a new current, if the list is empty it'll error out and thats how we know the list is done and we set current to none to break the loop.
# now we create two lists from the respective trees and return an expression that will either be true or false based how the lists match up.

# Complexities: 
#   space: O(N), q and p list created will be as long as the count of tree nodes
#   time: O(N), we got a while loop that goes through most of the list. 

#Note1: This line for some reason probably handles a weird edge case, it seems a bit unncessary for me to insert a value we most likely accounted for in while loop checking for either left or right.
