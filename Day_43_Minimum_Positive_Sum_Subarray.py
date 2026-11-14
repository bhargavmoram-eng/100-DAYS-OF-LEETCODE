class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        min_sum = float('inf')
        
        # Iterate through each possible subarray length from l to r
        for length in range(l, r + 1):
            # Calculate the sum of the first window of size 'length'
            current_sum = sum(nums[:length])
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)
            
            # Slide the window across the rest of the array
            for i in range(length, n):
                current_sum += nums[i] - nums[i - length]
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1
