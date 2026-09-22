class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        tar=[]
        for i in range(len(nums)):
            tar.insert(index[i],nums[i])
        return tar

        