class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1= max(nums)
        m2, m3, flag= float('-inf'), float('-inf'), 0

        for x in nums:
            if x!=m1 and x>m2:
                m2=x
        for x in nums:
            if x!=m1 and x!=m2 and x>m3:
                m3=x
                flag=1

        if flag==0:
            return m1
        else:
            return m3
        