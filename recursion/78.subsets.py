class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, ans=[], []

        def sub(ans,nums,idx):
            if idx== len(nums):
                res.append(ans[:])
                return

            ans.append(nums[idx])
            sub(ans,nums,idx+1)

            ans.remove(nums[idx])
            sub(ans,nums,idx+1)
            return res
        
        sub(ans,nums,0)
        return res