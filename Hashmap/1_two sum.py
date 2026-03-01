class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in dic:
                return [dic[complement],i]
            dic[num]=i
        return None