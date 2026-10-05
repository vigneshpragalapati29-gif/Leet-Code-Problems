class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        al="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while left<right:
            if s[left] not in al:
                left=left+1
            elif s[right] not in al:
                right=right-1
            else:
                s[left],s[right]=s[right],s[left]
                left=left+1
                right=right-1
        return "".join(s)

        
        