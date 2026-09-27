class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d={}
        su=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in nums:
            if d.get(i)==1:
                su=su+i
        return su

        