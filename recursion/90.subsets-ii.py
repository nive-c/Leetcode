class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,ans = [],[]

        def sub(nums,ans,idx):
            if idx>=len(nums):
                if ans in res:
                    return
                else:
                    res.append(ans[:])
                    return
            
            ans.append(nums[idx])
            sub(nums,ans,idx+1)

            ans.remove(nums[idx])
            sub(nums,ans,idx+1)

            return res

        nums.sort()
        sub(nums,ans,0)
        return res