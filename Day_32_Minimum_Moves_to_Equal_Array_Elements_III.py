class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        max_val = max(nums)
        return sum(max_val - num for num in nums)
