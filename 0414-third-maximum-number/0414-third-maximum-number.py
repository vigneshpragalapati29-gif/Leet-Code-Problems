class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s=sorted(set(nums))
        if len(s)>=3:
            return s[len(s)-3]
        else:
            return max(s)