class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[0]*n
        bit=0
        for i in range(n):
            nums[i]=start + 2*i
            bit ^=nums[i]
        return bit
        