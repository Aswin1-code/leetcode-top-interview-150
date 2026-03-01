class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl=list(s.lower())[::-1]
        c=0
        f=[]
        for i in (sl):
            if i.isalpha():
                f.append(i)
                c=1
            if i==' ' and c==1:
                break
        return len(f)
        
s=Solution()
s.lengthOfLastWord( "   fly me   to   the moon  ")
