class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl=list(s)
        ss=[]
        for i in sl:
           if i.isalnum():
               ss.append(i.lower())
        #print(ss)
        return True if ss==ss[::-1] else False
s=Solution()
s.isPalindrome("Race a car")