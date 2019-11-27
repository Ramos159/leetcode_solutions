# 2. Add Two Numbers

# Description: 

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Success:
# Runtime: 56 ms, faster than 99.43% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_number(node):
            val = ''
            while node:
                val += str(node.val)
                node = node.next
            return int(val[::-1])
        
        answer = ListNode(0)
        current = answer
        
        for num in str(get_number(l1) + get_number(l2))[::-1]:
            current.next = ListNode(int(num))
            current = current.next
        
        return answer.next

# Explanation: 

# I make a function whose sole purpose is just get me the number i need for each linked list.
# get_number use a string as a suedo list to append my numbers to, then cast the reverse string using list sling to an int.
# the loop says while node is a truthy value and not something like None, do this.
# this being add this node value to the string as a string, the next node is node.next .
# Initiate a Singly Linked List with answer, ListNode needs a starting number so i give it 0. 
# Current serves a pointer to the current node im dealing with and is used in loop below to keep track of where i am in the list.
# To start the for loop i iterate over a string which happens to be the value of both list numbers added together in reverse using list slicing again.
# In the loop i take current, assign their next attribute to be a new list node with value of num cast into a int.
# I change current to be the next value of itself and repeat the loop until its done. 
# Remember that we instantied the list with an value that means nothing to us. We can not return just answer for this reason, it has to be answer.next cause thats where we started adding our values. 

# Complexities: 
#   Space: O(N). Answer will be as long as the number of digits in the sum of get_number(l1) and get_number(l2).
#   Time: O(N). No matter what i'm going through the list to find their numbers then going through the entire sum string for the answer.