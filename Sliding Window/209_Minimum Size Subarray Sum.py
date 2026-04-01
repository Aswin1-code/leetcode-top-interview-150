class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # Sliding Window / Two Pointers
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # While the current window sum is >= target, shrink it from the left
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # If min_length was never updated, return 0
        return min_length if min_length != float('inf') else 0
