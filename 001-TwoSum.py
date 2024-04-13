class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 0
        for n in nums:
            for k in nums:
                if k + n == target and i is not j:
                    return i,j
                else:
                    j = j+1
            i = i+1    
            j=0
        
