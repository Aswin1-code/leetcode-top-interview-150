from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = Counter(magazine)
        ransom_counts = Counter(ransomNote)
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False
        return True
