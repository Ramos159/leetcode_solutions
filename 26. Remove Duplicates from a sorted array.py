# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.
# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

# Success:
# Runtime: 72 ms, faster than 99.76% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        current_index = 1
        current = nums[0]

        for index in range(len(nums)):

            if current != nums[index]:

                nums[current_index] = nums[index]
                current = nums[index]
                current_index += 1

        return current_index

# Explanation:

# we start with an edge case here, if the nums array is empty just send back 0,
# we then have then have two variables here, one to keep track of the current index we'll be working on on
# the other variable just looks after the current value we're on
# we use a range here to represent the indexes of num we'll be using and call the place holder for each instance index
# the condition we're testing says if current doesnt equal to the thing in nums at this index.
# here we're really saying we dont care for things that are equal to current and talk to me when you find something that doesnt equal current
# and when we do find something different we first make the current index place in nums the value in nums[index]
# after we say the current value is the one at nums[index] and we bump up the current_index number by one.
# when all is said and done we should have an array that doesnt contain any duplicates and we can return current_index cause that should be the number representing the index of the last number in our new nums

# Complexities: 
#   Space: O(1), we only use 2 int's at all times.
#   Time: O(N), we have to go through the entire nums list. 
