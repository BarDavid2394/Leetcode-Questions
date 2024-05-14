class Solution(object):
    def isValid(self, s):
        brackets = []
        Mymap = {')':'(','}':'{',']':'['}
        for c in s:
            if c in Mymap.values():
                brackets.append(c)
            if c in Mymap.keys():
                if not brackets or Mymap[c] != brackets.pop():
                    return False
        return not brackets
        













        # stack = []
        # Mymap = {')':'(', '}':'{',']':'['}
        # for c in s:
        #     if c in Mymap.values():
        #         stack.append(c)
        #     elif c in Mymap.keys():
        #         if not stack or stack.pop() != Mymap[c]:
        #             return False
        # return not stack
        # for c in s:
        #     if c in '[{(':
        #         stack.append(c)
        #         continue
        #     if c in ']})':
        #         if not stack:
        #             return False
        #         if  c == ']' and stack.pop() != '[':
        #             return False
        #         if  c == '}' and stack.pop() != '{':
        #             return False
        #         if  c == ')' and stack.pop() != '(':
        #             return False                
        # return not stack
        #same Runtime but the first code much prettier