class Solution(object):
    def reverse(self,string):
        return string[::-1]
    def reversePrefix(self, word, ch):
        for i in range(len(word)) :
            if(word[i] == ch):
                 return self.reverse(word[0:i+1]) + word[i+1:len(word)]
        return word

