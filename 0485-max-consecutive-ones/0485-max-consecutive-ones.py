class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        coun=0
        maxc=0
        for i in nums:
            if i==1:
                coun=coun+1
            maxc=max(coun,maxc)
            if i==0:
                coun=0
        return maxc
        

        
        