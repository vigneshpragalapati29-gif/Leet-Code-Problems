class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        d={}
        li=[]
        for i in nums:
           d[i]=d.get(i,0)+1
        for i in range(1,len(nums)+1):
            if d.get(i,0)==2:
                dup=i
            if d.get(i,0)==0:
                mis=i

               
        return [dup,mis]
        