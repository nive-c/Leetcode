class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n= len(nums)-1
        lst=[0]*(n+1)
        k=n
        i,j=0,n

        while i<=j:
            if abs(nums[i])>= abs(nums[j]):
                lst[k]= nums[i]**2
                i+=1
            elif abs(nums[j])> abs(nums[i]):
                lst[k]= nums[j]**2
                j-=1
            k-=1

        return lst
