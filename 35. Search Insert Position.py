# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

# Success:
# Runtime: 48 ms, faster than 90.78% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Search Insert Position

class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)

        while start < end:
            mid_index = start + (end - start)//2
            mid_value = nums[mid_index]

            if mid_value < target:
                start = mid_index+1
            elif mid_value > target:
                end = mid_index
            else:
                return mid_index
                
        return end

# Explanation:

# we start with two variables start and end, we give start 0 always to represent the front of the list
# we give end the size of the nums list
# in the while loop we do some funky stuff so bear with me,
# mid_index should be the middle number inbetween start and end, using some arithmetic we find the middle number
# mid_value should be the value in the nums array that is indexed at mid_index
# we start with some comparisons, first one is if mid_value is less than target our starting number will be the mid index + 1.
# this should skip over the middle number we have and go into the greater numbers that we want.
# the next comparison asks if mid_value is greater than target, if so end just becomes mid_index.
# the else deals with the case if the mid_value and target match up, we just return the mid_index.
# if for some reason we never find the value we wanted, we should have found the index which it should be inserted at via the end variable
# so we just return end  as such

# Complexities:
#   space: O(1) extra space, we only use two int variables the entire time.
#   time: O(log N), we use a binary search that runs at logarithmic time, we can do so because the array is sorted.
