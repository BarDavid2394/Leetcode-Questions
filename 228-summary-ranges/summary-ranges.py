class Solution(object):
    def summaryRanges(self, nums):
        n = len(nums)
        if n == 0 :
            return []
        list = []
        if n == 1:
            return [str(nums[0])]

        for i,num in enumerate(nums):
            if i==0:
                left = i
                continue
            if num != nums[i-1] + 1:
                if left == i-1:
                    list.append(str(nums[left]))
                else:
                    list.append(str(nums[left]) + "->" + str(nums[i-1]))
                left = i
            if i == n-1:
                if left == i:
                    list.append(str(num))
                else:
                    list.append(str(nums[left]) + "->" + str(num))
        return list
                

            

