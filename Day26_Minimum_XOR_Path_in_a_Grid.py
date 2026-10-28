class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[j] stores the set of all achievable XOR values for the current row
        dp = [set() for _ in range(n)]
        
        # Initialize the top-left starting cell
        dp[0].add(grid[0][0])
        
        # Initialize the first row (can only move right)
        for j in range(1, n):
            val = grid[0][j]
            for x in dp[j-1]:
                dp[j].add(x ^ val)
                
        # Fill the rest of the grid row by row
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            
            # First column of the current row (can only come from above)
            val = grid[i][0]
            for x in dp[0]:
                new_dp[0].add(x ^ val)
                
            # Fill remaining columns in the current row
            for j in range(1, n):
                val = grid[i][j]
                # Come from the top cell
                for x in dp[j]:
                    new_dp[j].add(x ^ val)
                # Come from the left cell
                for x in new_dp[j-1]:
                    new_dp[j].add(x ^ val)
            
            dp = new_dp
            
        # The result is the minimum value in the bottom-right cell's set
        return min(dp[-1])
