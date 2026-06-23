class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=0
        for x in s:
            res^=ord(x)
        for x in t:
            res^=ord(x)
        return chr(res)