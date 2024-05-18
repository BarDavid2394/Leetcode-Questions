class Solution(object):
    def removeStars(self, s):
        string_stack = []
        for c in s:
            if c == '*':
                string_stack.pop()
            else:
                string_stack.append(c)
        return ''.join(string_stack)

        """
        :type s: str
        :rtype: str
        """
        