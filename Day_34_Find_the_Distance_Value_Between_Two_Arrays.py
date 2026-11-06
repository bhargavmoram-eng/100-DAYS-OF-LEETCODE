import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find insertion point for the lower boundary (x - d)
            idx = bisect.bisect_left(arr2, x - d)
            
            # If no element in arr2 falls within [x - d, x + d], it's valid
            if idx == len(arr2) or arr2[idx] > x + d:
                distance_value += 1
                
        return distance_value
