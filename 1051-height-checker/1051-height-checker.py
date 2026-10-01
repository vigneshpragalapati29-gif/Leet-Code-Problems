class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        li=sorted(heights)
        c=0
        for i in range(len(li)):
            if li[i]!=heights[i]:
                c=c+1
        return c
        