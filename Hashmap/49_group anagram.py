from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        r_map=defaultdict(list)
        ans=[]
        for i in strs:
            a=sorted(i)
            r_map[tuple(a)].append(i)
        for val in r_map.values():
            ans.append(val)
        return ans
