class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        li=[]
        d={}
        x=True
        for i in arr:
            d[i]=d.get(i,0)+1
        for i in d.values():
            if i not in li:
                li.append(i)
            else:
                x=False
        return x

        
