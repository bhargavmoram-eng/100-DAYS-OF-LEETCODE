class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: if out of bounds or water, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            # Mark the current land cell as visited by turning it to water
            grid[r][c] = 1
            # Visit all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Flood-fill all land connected to the boundaries
        for r in range(rows):
            for c in range(cols):
                # Check if the cell is on the border and is land
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r, c)
                    
        # Step 2: Count the remaining closed islands
        closed_islands_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    dfs(r, c) # Sink the visited closed island
                    
        return closed_islands_count
