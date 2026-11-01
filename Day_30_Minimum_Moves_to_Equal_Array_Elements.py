class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the minimum value in the array
        min_val = min(nums)
        
        # Sum the differences between each element and the minimum value
        return sum(num - min_val for num in nums)
