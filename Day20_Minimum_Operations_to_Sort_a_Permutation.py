from collections import deque

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        # Find the index of 0 in the input array
        idx0 = nums.index(0)
        
        # Check if the input matches the Increasing family
        is_inc = True
        for i in range(n):
            if nums[(idx0 + i) % n] != i:
                is_inc = False
                break
                
        # Check if the input matches the Decreasing family
        is_dec = True
        for i in range(n):
            if nums[(idx0 - i) % n] != i:
                is_dec = False
                break
                
        # If it doesn't match either, it's impossible to sort
        if not is_inc and not is_dec:
            return -1
            
        # BFS to find the shortest path from the sorted target (0, 0) to all states
        dist = {}
        queue = deque([(0, 0, 0)])  # (is_decreasing, idx_of_0, distance)
        dist[(0, 0)] = 0
        
        while queue:
            t, x, d = queue.popleft()
            
            # Predecessor via Left Rotate (moving backward means Right Rotate)
            nx1 = (x + 1) % n
            if (t, nx1) not in dist:
                dist[(t, nx1)] = d + 1
                queue.append((t, nx1, d + 1))
                
            # Predecessor via Reverse (Reverse is its own inverse)
            nt2 = 1 - t
            nx2 = (n - 1 - x) % n
            if (nt2, nx2) not in dist:
                dist[(nt2, nx2)] = d + 1
                queue.append((nt2, nx2, d + 1))
                
        # Collect the minimum operations required for the matching initial state(s)
        ans = float('inf')
        if is_inc and (0, idx0) in dist:
            ans = min(ans, dist[(0, idx0)])
        if is_dec and (1, idx0) in dist:
            ans = min(ans, dist[(1, idx0)])
            
        return ans if ans != float('inf') else -1
