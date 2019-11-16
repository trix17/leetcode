#3. Longest Substring Without Repeating Characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0 
        maximum = 0 
        set = dict() # create a hashset or dict to keeep track of evrything
        
        for end in range (len(s)):
        
