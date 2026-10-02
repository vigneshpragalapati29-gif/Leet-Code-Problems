class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftsum=0
        tot=sum(nums)
        for i in range(len(nums)):
            rightsum=tot-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1

        
        

        