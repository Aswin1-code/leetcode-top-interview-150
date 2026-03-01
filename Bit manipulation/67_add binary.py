class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2)+int(b,2)))[2::]
s=Solution()
s.addBinary("11", "1") 