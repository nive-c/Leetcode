class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=res=0

        while i<len(nums):
            if nums[i]==0:
                i+=1
                continue
            j=i

            while j<len(nums) and nums[j]==1:
                j+=1
            res=max(j-i,res)
            i=j

        return res