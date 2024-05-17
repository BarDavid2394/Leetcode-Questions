class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #we find the max at one run. then return a list with the answers
        max_candy = max(candies)
        res = []
        for kid in candies:
            if kid + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
        return res
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        