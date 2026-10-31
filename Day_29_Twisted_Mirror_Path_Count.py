class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        memo = {}
        
        # Helper function to simulate the path until hitting a decision point or terminating
        def get_landing_cell(r, c, direction):
            if direction == 'R':
                nr, nc = r, c + 1
            else:
                nr, nc = r + 1, c
                
            while True:
                # Out of bounds check
                if nr >= m or nc >= n:
                    return None
                # Reached the destination
                if nr == m - 1 and nc == n - 1:
                    return (nr, nc)
                # Reached an empty cell (new decision point)
                if grid[nr][nc] == 0:
                    return (nr, nc)
                
                # Reflect off the mirror
                if direction == 'R':
                    nr, nc = nr + 1, nc
                    direction = 'D'
                else:
                    nr, nc = nr, nc + 1
                    direction = 'R'

        # Depth-First Search with Memoization
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            
            total_paths = 0
            
            # 1. Try moving Right
            next_r = get_landing_cell(r, c, 'R')
            if next_r:
                total_paths = (total_paths + dfs(next_r[0], next_r[1])) % MOD
                
            # 2. Try moving Down
            next_d = get_landing_cell(r, c, 'D')
            if next_d:
                total_paths = (total_paths + dfs(next_d[0], next_d[1])) % MOD
                
            memo[(r, c)] = total_paths
            return total_paths

        return dfs(0, 0)
