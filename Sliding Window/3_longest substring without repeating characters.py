from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_map = {}
        left = 0 
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length