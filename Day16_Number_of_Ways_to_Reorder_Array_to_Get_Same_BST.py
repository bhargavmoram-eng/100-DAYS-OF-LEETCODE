import math

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Helper function to calculate combinations nCr
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            # Use the manual nCr function instead of math.comb
            interleave_ways = nCr(len(left) + len(right), len(left))
            
            return (interleave_ways * left_ways * right_ways) % MOD
            
        return (dfs(nums) - 1) % MOD
