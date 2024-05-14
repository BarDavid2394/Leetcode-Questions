class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum = 0
            for c in str(n):
                sum += pow(int(c),2)
            n = sum
        return n == 1

        """
        :type n: int
        :rtype: bool
        """
        