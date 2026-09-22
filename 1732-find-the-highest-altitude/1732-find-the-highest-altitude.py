class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr=0
        maxc=0
        for i in range(len(gain)):
            curr=curr+gain[i]
            maxc=max(maxc,curr)
        return maxc