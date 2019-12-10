# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# Success: 

# Runtime: 132 ms, faster than 97.85% of Python3 online submissions for Missing Number.
# Memory Usage: 14.5 MB, less than 11.29% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = len(nums) + 1
        
        for number in range(length):
            if number not in nums_set: 
                return number

# Explanation: 

# Not going to lie this question kinda sucked just because the test case inputs didnt matchup as described.
# They didn't explain that there would be duplicates, but there are in the tests. 
# So to counteract the duplicates, make a nice set from the nums parameter we get.
# afterwards, its told to us that only a single number would be missing. 
# using this bit of knowledge we can gather the range we need to iterate through by just getting the length of the set plus 1
# the extra one is here to account for the single missing number we need to find.
# now in a for loop in a our range of length, we check to see if the number we currently have is in the set we created.
# If the number we have is not in the set, thats the number were looking for and we return.
# if not keep searching.

# Complexities:
#   space: O(N) for the set can technically be as big as the nums parameter.
#   time: O(N) cause we have to go through at the very worst the entire range to find the missing number.