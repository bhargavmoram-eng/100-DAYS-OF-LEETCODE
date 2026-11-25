class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Double hashing parameters to prevent collisions
        base1, mod1 = 1315423911, 10**9 + 7
        base2, mod2 = 100003, 10**9 + 9

        def has_unique_of_length(length):
            h1 = h2 = 0
            p1 = pow(base1, length - 1, mod1)
            p2 = pow(base2, length - 1, mod2)
            
            # Compute initial window hash
            for i in range(length):
                # Add a small offset (e.g., +1) in case nums contains 0
                val = nums[i] + 1
                h1 = (h1 * base1 + val) % mod1
                h2 = (h2 * base2 + val) % mod2
                
            counts = {(h1, h2): 1}
            
            # Slide window across the array
            for i in range(length, n):
                left_val = nums[i - length] + 1
                right_val = nums[i] + 1
                
                h1 = ((h1 - left_val * p1) * base1 + right_val) % mod1
                h2 = ((h2 - left_val * p2) * base2 + right_val) % mod2
                
                state = (h1, h2)
                counts[state] = counts.get(state, 0) + 1
                
            # Check if any subarray hash occurred exactly once
            return any(freq == 1 for freq in counts.values())

        left, right = 1, n
        ans = n
        
        while left <= right:
            mid = (left + right) // 2
            if has_unique_of_length(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller valid length
            else:
                left = mid + 1   # Need a longer subarray to make it unique
                
        return ans
