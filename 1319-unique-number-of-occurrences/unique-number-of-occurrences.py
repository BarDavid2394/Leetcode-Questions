class Solution(object):
    def uniqueOccurrences(self, arr):
        Mymap= {}
        for num in arr:
            Mymap[num] = 1 if num not in Mymap else Mymap[num] + 1
        Seen = []
        for value in Mymap.values():
            if value in Seen:
                return False
            else:
                Seen.append(value)
        return True

        """
        :type arr: List[int]
        :rtype: bool
        """
        