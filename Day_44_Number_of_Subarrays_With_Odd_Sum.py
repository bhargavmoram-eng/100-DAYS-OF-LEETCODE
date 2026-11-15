class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        even_count = 1  # Prefix sum of 0 is even
        odd_count = 0
        current_sum = 0
        ans = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1
                
        return ans % MOD
