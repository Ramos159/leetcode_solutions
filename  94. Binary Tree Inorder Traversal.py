# Description: Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Success:

# Runtime: 20 ms, faster than 97.03% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        answer = []
        self.helper(root,answer)
        return answer
    
    def helper(self,node,answer):
        if node:
            self.helper(node.left,answer)
            answer.append(node.val)
            self.helper(node.right,answer)


# Explanation: 

# this one is pretty easy honestly using recurssion.
# you set up a list to be the answer you want to return
# you have a helper function that does most of the work.
# you run the function with the root and the answer list
# inside the helper since we check if node is valid object, cause we might send something null
# if node isnt null we check if it has a left. if it does we run the function again with the left node.
# we add the current value to answer since we checked for left
# if node has a right we do the samething with left but with right.
# after were done, return answer

# Complexities:
#   Space: O(N), bigger the tree the more space we need for answer and recurssion
#   Time: O(N), bigger the tree the more functions we will run to account for them.

# Follow up: 

# Runtime: 24 ms, faster than 87.51% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        answer = []
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            answer.append(root.val)
            
            root = root.right
        
        return answer

# Explanation:

# anything that can be done recursively can be done iteratively, and so we have a challenge
# we start with a stack and answer list. like last solution we're gonna return answer at the end
# we use a while with the condition that checks for a root or stack, if a stack is empty its false.
# so if we have a root go through all the possible left nodes.
# if you get the a null node we stop and pop the stack to get the last node we had.
# we log the node in answer cause its the left most node.
# then all we say is root is now the right one, if thats null than we just pop the stack and go again. 
# at the end of it all we should have a nice array to return