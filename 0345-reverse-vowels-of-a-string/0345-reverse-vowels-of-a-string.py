class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        li=list(s)
        left=0
        right=len(li)-1
        while left<right:
            if li[left] not in v:
                left=left+1
            elif li[right] not in v:
                right=right-1
            else :
                li[left],li[right] = li[right],li[left]
                left=left+1
                right=right-1
        return "".join(li)
        
      
        