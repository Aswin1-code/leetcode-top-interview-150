from collections import defaultdict
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return((len(nums)))
        
s=Solution()        
s.removeElement([3,2,2,3],3)
