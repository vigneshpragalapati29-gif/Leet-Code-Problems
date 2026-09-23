class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s=1
        if num<=1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                s+=i
                s+=num//i
        if s==num:
            return True
        return False
            

        