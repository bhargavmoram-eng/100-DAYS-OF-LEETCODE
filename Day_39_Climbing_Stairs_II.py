class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # Base case: if we are already at step 0, cost is 0
        if n == 0:
            return 0
        
        # Initialize the dp array with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Compute the minimum cost for each step up to n
        for i in range(1, n + 1):
            cost_i = costs[i - 1]  # 1-indexed to 0-indexed adjustment
            
            # Jump of 1 step (from i - 1)
            if i >= 1:
                dp[i] = min(dp[i], dp[i - 1] + cost_i + 1)
                
            # Jump of 2 steps (from i - 2)
            if i >= 2:
                dp[i] = min(dp[i], dp[i - 2] + cost_i + 4)
                
            # Jump of 3 steps (from i - 3)
            if i >= 3:
                dp[i] = min(dp[i], dp[i - 3] + cost_i + 9)
                
        return dp[n]
