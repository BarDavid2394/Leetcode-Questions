class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words_stack = []
        res = ""
        for word in words:
            words_stack.append(word)
        for i in range(len(words_stack)):
            if i != 0:
                res += " "
            res += words_stack.pop()
        return res

    
        """
        :type s: str
        :rtype: str
        """
        