class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize ans to -1 (in binary, -1 has all bits set to 1)
        ans = -1
        
        for i, x in enumerate(nums):
            # Check if the element is out of its sorted position
            if i != x:
                ans &= x
                
        # If the array is already sorted, ans remains -1, so we return 0
        return max(ans, 0)
