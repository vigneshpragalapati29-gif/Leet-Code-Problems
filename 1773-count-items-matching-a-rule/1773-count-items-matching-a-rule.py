class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        i=0
        c=0
        if ruleKey=="type":
            i=0
        elif ruleKey=="color":
            i=1
        else:
            i=2
        for j in range(len(items)):
            if items[j][i]==ruleValue:
                c+=1
        return c
        