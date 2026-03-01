class Solution:
    def reverseBits(self, n: int) -> int:
        b="{:032b}".format(n)
        r=b[::-1]
        return int(r,2)
        