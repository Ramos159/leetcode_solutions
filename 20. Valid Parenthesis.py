# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

# Success:
# Runtime: 20 ms, faster than 99.01% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses

class Solution:
    def isValid(self,s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for char in s:

            if char not in table:
                stack.append(char)
                    
            else:
                try:
                    first = stack.pop()
                except:
                    first = None
                    
                if table[char] != first:
                    return False
                        
        return not stack

# Explanation: 

# we start with a list that will be used as a stack, we use a stack because we need to able to push and access the top of the list frequently
# i create a small dictionary for us to be able to reference all the opening parenthesis and theyre matching counterparts
# we start a for loop going through the entire string and we check each time if we have a key in table matching our current char
# if so we just put it on to the stack list we have
# if not we attempt to get a valid char from the top of the list, if we cant get one first is just None
# if the value-pair in table for the key of char doesnt match the char we have in first return false and we do nothing afterwards.
# After we finish the we loop have to assess the remaining stack. If the stack is empty then we had a valid string and if its not empty we have a bad one.
# playing around with truthy values in python we can return not stack. 
# an empty stack when used an expression is false, and the inverse is true hence why we use not in our return.

# Complextities:
#     space: O(N), the stack can be as big as the string in its worst cases.
#     time: O(N), we also have to loop throuhg the entire string to if its valid. 