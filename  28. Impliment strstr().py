# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Success:
# Runtime: 28 ms, faster than 89.50% of Python3 online submissions for Implement strStr().
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if str == '':
            return 0
        
        index = -1
        
        for i in range(len(haystack)-(len(needle)-1)):
            current = haystack[i:(len(needle)+i)]
            
            if current == needle:
                index = i
                break
        
        return index

# Explanation:

# we start with an edge for which the answer was given to us. if we get an empty string just return 0
# then we set a variable with name index to -1, to indicate no instance of needle in haystack.
# we loop over a range here that is length of haystack minus the length of the needle - 1. 
# this is to represent the amount of room we have to shift around for our current variable. if we have a length of 10 in the haystack but our needle is 5 chars long, we can only test 5 possible substrings.
# line 32 we make the current substring to test, if current and needle are a match we update index and break the loop and return index.
# if we never find a match we return the index anyway cause its set to -1. 

# Complexities:
#   Space: O(1), we only use index that will always hold an int.
#   Time: O(N), worst case you're going through the entire string to find no match.