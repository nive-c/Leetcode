class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            i,j= 0,len(x)-1
            flag=0
            while(i<j):
                if x[i]!=x[j]:
                    flag=1
                    break
                i+=1
                j-=1
            if flag==0:
                return x
        
        return ""