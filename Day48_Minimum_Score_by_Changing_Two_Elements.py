class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(
            nums[-1] - nums[2],  # Change 2 smallest
            nums[-3] - nums[0],  # Change 2 largest
            nums[-2] - nums[1]   # Change 1 smallest and 1 largest
        )
