class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = {}
        
        for num in nums:
            # Option 1: Increase num by 1 (extends sequence ending at num)
            dp[num + 1] = dp.get(num, 0) + 1
            
            # Option 2: Keep num unchanged (extends sequence ending at num - 1)
            dp[num] = dp.get(num - 1, 0) + 1
            
        return max(dp.values())
