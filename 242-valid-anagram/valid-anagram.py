# import collections
class Solution(object):
    def isAnagram(self, s, t):
      Mymap = {}
      for c  in s:
        Mymap[c] = 1 if c not in Mymap else  Mymap[c] + 1
      for c  in t:
        Mymap[c] = -1 if c not in Mymap else  Mymap[c] - 1
      return all(value == 0 for value in Mymap.values())



               

        