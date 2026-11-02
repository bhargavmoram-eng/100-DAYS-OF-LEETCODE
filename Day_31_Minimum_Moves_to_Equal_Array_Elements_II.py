class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array to easily find the median
        nums.sort()
        
        # Step 2: Identify the median element
        median = nums[len(nums) // 2]
        
        # Step 3: Sum the absolute differences from the median
        return sum(abs(num - median) for num in nums)
