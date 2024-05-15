class Solution(object):
    def groupAnagrams(self, strs):
        Mymap = defaultdict(list)
        for word in strs:
            Mymap[tuple(sorted(word))].append(word)
        return list(Mymap.values())

         




        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        