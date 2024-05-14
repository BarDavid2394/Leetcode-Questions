class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        last_element = strs[len(strs)-1]
        first = strs[0]
        string = ''
        for i in range(len(strs[0])):
            if first[i] == last_element[i]:
                 string+= first[i]
            else:
                 return string
        return string

            




















        # strs.sort()
        # result,index = "",0
        # first, last = strs[0], strs[(len(strs)-1)]
        # while index< min(len(first),len(last)):
        #     if first[index] == last[index]:
        #         result += first[index]
        #     else:
        #         break
        #     index += 1
        # return result
        
        
                #i can sort the array and then go through the first and the last word - no need to work on the strings in between