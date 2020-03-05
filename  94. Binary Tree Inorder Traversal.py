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

# follow up: 

# comming soon
