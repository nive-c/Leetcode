class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for x in accounts:
            wealth=max(sum(x),wealth)

        return wealth