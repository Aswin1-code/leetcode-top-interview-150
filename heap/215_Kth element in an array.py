class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l=sorted(nums,reverse=True)
        return l[k-1]