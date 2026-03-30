class Solution:
    def romanToInt(self, s: str) -> int:
        r_map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev_val,pres_val=0,0
        tot=0
        for i in reversed(s):
            pres_val=r_map.get(i)
            if pres_val<prev_val:
                tot-=pres_val
            else:
                tot+=pres_val
                prev_val=pres_val
        return tot
