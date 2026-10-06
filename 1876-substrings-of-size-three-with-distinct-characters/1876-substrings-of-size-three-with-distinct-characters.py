class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        x=""
        c=0
        for i in range(len(s)-2):
            x=s[i]+s[i+1]+s[i+2]
            k=set(x)
            if len(k)==3:
                c=c+1
        return c


        