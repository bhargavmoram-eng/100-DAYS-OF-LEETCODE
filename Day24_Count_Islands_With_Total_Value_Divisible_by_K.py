class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        divisible_island_count = 0
        
        for r in range(m):
            for c in range(n):
                # Found an unvisited piece of land (positive integer)
                if grid[r][c] > 0 and not visited[r][c]:
                    total_value = 0
                    stack = [(r, c)]
                    visited[r][c] = True
                    
                    # Iterative DFS to find all connected parts of the island
                    while stack:
                        curr_r, curr_c = stack.pop()
                        total_value += grid[curr_r][curr_c]
                        
                        # Explore 4-directional neighbors
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] > 0 and not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc))
                    
                    # Check if the island's total sum is divisible by k
                    if total_value % k == 0:
                        divisible_island_count += 1
                        
        return divisible_island_count
