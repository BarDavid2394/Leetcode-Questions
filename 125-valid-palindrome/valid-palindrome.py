class Solution(object):
    def isPalindrome(self, s):
        s = [i for i in s.lower() if  i.isalnum()]
        return s == s[::-1]
        """
        :type s: str
        :rtype: bool
        """
        