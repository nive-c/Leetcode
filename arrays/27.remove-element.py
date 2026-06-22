class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx,count=0,0
        for x in nums:
            if x==val:
                count+=1
            else:
                nums[idx]=x
                idx+=1
        return idx