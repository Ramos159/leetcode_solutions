# Description:

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Success: IN ONE PASS

# Runtime: 20 ms, faster than 99.87% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        trailer = head
        counter = 0
        
        while current:
            if counter > n:
                trailer = trailer.next
            counter += 1
            current = current.next
            
        if counter == n:
            return head.next
        else:
            trailer.next = trailer.next.next
            return head


# Explanation:

# We start with two pointers. one that will keep track of the current node were on until the end and one that trail behind N nodes.
# We use a counter just to keep track of when we should start moving trailer up.
# we use a while loop to go through the entire list, we check to see if the counter is up to our N parameter. If it is we start moving our trailer up the list.
# After our IF statement we then increase our counter by 1 and move our current up the list.
# After we exit our loop we should be at the end of the list with the trailer being the node whose next we need to change.

# There's a small edge case we have to consider if N turns out to be the head node number we have no way to reference it.
# If N turns out to be the head node, and we can check if it is if the counter at the end of the loop equal ends
# If they are equal then were looking to remove the head node since N in this case is the first thing in the list.
# In this case we just turn the head's next element with head.next

# If our edge case doesnt work out, we can assume it isnt the head and we just take our trailer's next and set it to be the next nodes next
# This will remove the node in memory from the list and give us the answer we need.

# Complexities: 
#   space: O(1), no extra space is needed. two pointers will always reference one node at a time, and the counter will always be a number.
#   time: O(N), We have to go through the entire list no matter what, So it is N with N being how long the list is. 