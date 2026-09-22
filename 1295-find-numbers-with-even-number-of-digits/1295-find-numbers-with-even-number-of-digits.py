class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        def number(num):
            d=int(math.log10(num))+1
            return d
        c=0
        for i in nums:
            if number(i) %2==0:
                c+=1
        return c
        