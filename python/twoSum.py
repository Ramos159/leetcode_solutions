# 1. Two Sum

# Description:

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Success
# Runtime: 48 ms, faster than 95.65% of Python3 online submissions for Two Sum.
# Memory Usage: 13.9 MB, less than 66.05% of Python3 online submissions for Two Sum.

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def find_pair(num,target):
            if num < target:
                return target - num
            elif num == target:
                return 0
            else:
                return target - num
            
        checker = {}
        
        for i,num in enumerate(nums):
            pair = find_pair(num,target)
            
            if pair in checker:
                return [checker[pair],i]
            else:
                checker[num] = i

# Explanation: 

# I started with writing the find_pair function.
# It would return me the correct pair needed add up to target based on the num i was iterating over.
# I would check to see if my dict "checker" has seen the pair i needed
# If it did not see the pair, i would store the num as the key, and its index as the value.
# If i did see the pair in checker, i would return a list with the current i and the value stored in the key of pair

#Complexity: 

# Worst case:
#   space: O(N), with the growing key and value entries the checker dict gets bigger
#   time: O(N), you might have to go through all the numbers in nums to find your pair