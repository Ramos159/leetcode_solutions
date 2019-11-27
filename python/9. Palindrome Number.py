# Description:

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Success: 

# Runtime: 56 ms, faster than 93.29% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Explanation:

# This one is pretty easy, turn the int into a string and list slice to get the reverse and return the comparison.

# Complexities:
#   Space: O(1), no extra space is needed.
#   Time: O(1), all there is, is a comparison between the two. 

