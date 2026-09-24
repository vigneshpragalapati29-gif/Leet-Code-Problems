class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        li=[]
        for i in digits:
            s+=str(i)
        x=int(s)+1
        y=str(x)
        for i in y:
            li.append(int(i))
        return li

        