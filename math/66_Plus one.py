class Solution:
    def plusOne(self, digits: list[int]) ->list[int]:
        s=digits
        a=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==9:
                s[i]=0
            else:
                s[i]+=1
                return s
        s.insert(0,1)
        return s    