class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        lst = [0]*n
        i,j= s.find(c),0
        k=0
        while i<n and j<n:
            while j<n and s[j]!=c :
                j+=1
            if j==len(s):
                while k<n:
                    lst[k]= abs(i-k)
                    k+=1
                break
            while k<=j:
                lst[k]= min(abs(i-k), abs(j-k))
                k+=1
            i=j
            j+=1

        return lst