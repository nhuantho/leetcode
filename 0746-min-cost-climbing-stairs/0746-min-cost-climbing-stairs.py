class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        dp = [0] * len_cost
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len_cost):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[-1], dp[-2])