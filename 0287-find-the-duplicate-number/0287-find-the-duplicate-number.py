class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in nums:
            if d.get(i)>1:
                return i
        