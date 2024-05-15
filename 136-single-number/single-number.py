class Solution(object):
    def singleNumber(self, nums):
        unique_num = 0
        for num in nums:
             unique_num ^= num
        return unique_num
        

        # a XOR a = 0, a XOR 0 = a, a XOR b = b XOR a, so it the order does not really matter.
        #after Xoring all the elements we'll stay with the unique one.