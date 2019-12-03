# Description:

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Success:

# Runtime: 32 ms, faster than 95.09% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        lst = ListNode(0)
        
        current = l1
        current2 = l2
        
        while(current or current2):
            try:
                arr.append(current.val)
                current = current.next
            except:
                pass
            
            try:
                arr.append(current2.val)
                current2 = current2.next
            except:
                pass
        
        arr.sort()
        
        holder = lst
        for num in arr:
            holder.next = ListNode(num)
            holder = holder.next
        
        return lst.next

# Explanation:

# We make an array to hold all the values contained in the lists and a new list to submit as an answer.
# Make use of two pointers for both lists and use a while to go through each list.
# Use try and catch to see if the lists are still valid, Its not guaranteed if the lists are equal in size.
# In the try we try to append the value the list node has and assign it to next, the catch would catch the error form the current/current2 assignment
# We would then sort with the python sort method, which has an N Log N time according to docs.
# we create a new pointer for us to use to append to our linkedlist properly called holder.
# use a for loop to go through the sorted numbers and append to our list.
# We return using lst.next cause we instantiated lst with an arbitrary number. 

# Complexities:
#   space: O(N), Our answer linkedlist and array will be as big as our two list inputs.
#   time: O(N), We use a while and a for loop to go through our lists and make a new one. 