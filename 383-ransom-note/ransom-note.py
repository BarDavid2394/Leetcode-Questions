class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        Mymap={}
        for c in magazine:
            Mymap[c] = 1 if c not in Mymap else Mymap[c] +1
        for c in ransomNote:
            if  c not in Mymap or Mymap[c] == 0:
                return False
            Mymap[c] -=1
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
