class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        x=sorted(nums)
        s=0
        for i in range(0,len(x),2):
            s+=x[i]
        return s
        