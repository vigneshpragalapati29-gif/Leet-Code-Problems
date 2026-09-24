class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d={}
        li=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d.get(i)>1:
                li.append(i)
        return li
        