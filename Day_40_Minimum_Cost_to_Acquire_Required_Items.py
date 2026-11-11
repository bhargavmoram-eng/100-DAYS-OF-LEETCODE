class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # Strategy 1: Buy only separate items
        option1 = need1 * cost1 + need2 * cost2
        
        # Strategy 2: Buy type 3 items up to the maximum required amount
        option2 = max(need1, need2) * costBoth
        
        # Strategy 3: Buy type 3 items up to the minimum required amount, 
        # and fulfill the rest with individual items
        common = min(need1, need2)
        option3 = common * costBoth + (need1 - common) * cost1 + (need2 - common) * cost2
        
        # Return the minimum among all three strategies
        return min(option1, option2, option3)
