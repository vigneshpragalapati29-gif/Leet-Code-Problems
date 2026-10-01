class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        add=0
        for i in range(len(s)):
            if i%2==0:
                add=add+int(s[i])
            else:
                add=add-int(s[i])
        return add        