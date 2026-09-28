class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        
        # Replace punctuation with spaces
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        
        ans = paragraph.lower().split()

        d = {}

        for i in ans:
            d[i] = d.get(i, 0) + 1

        while True:
            max_val = max(d, key=d.get)

            if max_val not in banned:
                return max_val
            else:
                del d[max_val]