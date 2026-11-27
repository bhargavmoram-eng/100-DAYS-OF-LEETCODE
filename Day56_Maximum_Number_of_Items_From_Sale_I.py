class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        
        # Step 1: Precompute the number of free items gained from buying item i once
        free = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1
                    
        # dp[b] = max items obtainable with exact or at most budget b
        dp = [0] * (budget + 1)
        
        # Step 2: Knapsack DP
        for i in range(n):
            cost = items[i][1]
            bonus = free[i]
            
            # 0/1 Knapsack step: Buying the FIRST copy of item i (gives 1 + bonus items)
            # Iterate backwards so we don't apply the bonus multiple times for item i
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + 1 + bonus)
                
            # Unbounded Knapsack step: Buying ADDITIONAL copies of item i (gives 1 item each)
            # Iterate forwards to allow unlimited copies
            for b in range(cost, budget + 1):
                dp[b] = max(dp[b], dp[b - cost] + 1)
                
        return dp[budget]
