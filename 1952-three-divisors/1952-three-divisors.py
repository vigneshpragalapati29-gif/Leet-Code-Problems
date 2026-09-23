class Solution:
    def isThree(self, n: int) -> bool:
        div=0
        i=1
        while i<=n:
            if n%i==0:
                div+=1
            i=i+1
        if div==3:
            return True
        return False
            
        