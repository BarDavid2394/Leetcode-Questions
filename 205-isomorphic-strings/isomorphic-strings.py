class Solution(object):
    def isIsomorphic(self, s, t):
        d1,d2 = {}, {}
        for i,c in enumerate(s):
            d1[c] = d1.get(c,[]) + [i]
        for i,c in enumerate(t):
            d2[c] = d2.get(c,[]) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
        