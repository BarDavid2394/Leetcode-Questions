class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1,-1,-1):
            digits[i] += 1
            if digits[i] == 10 :
                digits[i] = 0
                if i != 0:
                    continue
                else:
                    digits.insert(0,1)
                    return digits
            return digits


        """
        :type digits: List[int]
        :rtype: List[int]
        """
        