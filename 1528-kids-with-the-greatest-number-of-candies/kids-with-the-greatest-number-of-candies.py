class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #we find the max at one run. then return a list with the answers
        max_candy = max(candies)
        return[kid + extraCandies >= max_candy for kid in candies]
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        