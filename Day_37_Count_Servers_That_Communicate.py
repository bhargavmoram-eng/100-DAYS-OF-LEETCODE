class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        # Step 1: Precompute the number of servers in each row and column
        row_counts = [0] * num_rows
        col_counts = [0] * num_cols
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        # Step 2: Count all servers that share a row or column with another server
        communicating_servers = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
