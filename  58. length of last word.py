# Description:

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

# Success:
# Runtime: 24 ms, faster than 85.46% of Python3 online submissions for Length of Last Word.
# Memory Usage: 12.8 MB, less than 100% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            return len(s.split()[-1])
        except:
            return 0

# Explanation:

# This is rather easy honestly. You just split the string and return the length of the last word.
# The string might be empty, in that case you want to return 0. so we use a try and except.

# Complexities: 
#   Time: O(N). The way split works is that it basically runs at N, where N is how many substrings the seperator makes. We have to split the string and then return an ArrayList<str>, to then return the length of the last word in the list.
#   Space: O(N). This entirely depends on how big the Array of strings is, which is entirely dependent on how many legal words the string might have.     