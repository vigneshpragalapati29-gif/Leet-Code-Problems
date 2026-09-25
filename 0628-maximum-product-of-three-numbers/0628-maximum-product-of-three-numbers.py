class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        x=sorted(nums)
        n=len(x)
        return max(x[n-1]*x[n-2]*x[n-3],x[0]*x[1]*x[n-1])
        
        