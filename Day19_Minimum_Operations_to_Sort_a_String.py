class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # Case 0: Already sorted
        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        
        # Case -1: Unsorted string of length 2 cannot be changed
        if n == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # Case 1: First element is min OR last element is max
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # Case 2: Either mn or mx is present in the interior of the string
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
                
        # Case 3: All min characters are at the end and all max characters are at the start
        return 3
