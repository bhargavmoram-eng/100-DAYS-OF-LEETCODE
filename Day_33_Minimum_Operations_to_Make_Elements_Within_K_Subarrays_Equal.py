from sortedcontainers import SortedList

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < x * k:
            return -1

        lower = SortedList()
        upper = SortedList()
        
        state = {
            'lower_sum': 0,
            'upper_sum': 0
        }
        
        len_lower_target = (x + 1) // 2
        costs = [0] * (n - x + 1)
        
        def balance_and_sort():
            # 1. Ensure values are correctly separated between halves
            while lower and upper and lower[-1] > upper[0]:
                to_upper = lower.pop(-1)
                to_lower = upper.pop(0)
                
                state['lower_sum'] += to_lower - to_upper
                state['upper_sum'] += to_upper - to_lower
                
                lower.add(to_lower)
                upper.add(to_upper)
                
            # 2. Ensure sizes match targets
            while len(lower) > len_lower_target:
                val = lower.pop(-1)
                state['lower_sum'] -= val
                upper.add(val)
                state['upper_sum'] += val
                
            while len(lower) < len_lower_target and upper:
                val = upper.pop(0)
                state['upper_sum'] -= val
                lower.add(val)
                state['lower_sum'] += val

        # 1. Initialize the first window
        for i in range(x):
            num = nums[i]
            if not lower or num <= lower[-1]:
                lower.add(num)
                state['lower_sum'] += num
            else:
                upper.add(num)
                state['upper_sum'] += num
            balance_and_sort()
        
        median = lower[-1]
        costs[0] = (median * len(lower) - state['lower_sum']) + (state['upper_sum'] - median * len(upper))
        
        # 2. Slide the window across the remaining elements
        for i in range(1, n - x + 1):
            # Remove the element leaving the window
            rem = nums[i - 1]
            if upper and rem >= upper[0]:
                upper.remove(rem)
                state['upper_sum'] -= rem
            else:
                lower.remove(rem)
                state['lower_sum'] -= rem
                
            # Add the element entering the window
            add = nums[i + x - 1]
            if not lower or add <= lower[-1]:
                lower.add(add)
                state['lower_sum'] += add
            else:
                upper.add(add)
                state['upper_sum'] += add
                
            balance_and_sort()
                
            median = lower[-1]
            costs[i] = (median * len(lower) - state['lower_sum']) + (state['upper_sum'] - median * len(upper))
            
        # 3. Dynamic Programming to select k non-overlapping subarrays
        INF = float('inf')
        dp_table = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp_table[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option A: Skip the current element
                dp_table[i][j] = dp_table[i - 1][j]
                
                # Option B: Pick the window ending at index i-1
                if i >= x:
                    cost_idx = i - x
                    if dp_table[cost_idx][j - 1] != INF:
                        dp_table[i][j] = min(dp_table[i][j], dp_table[cost_idx][j - 1] + costs[cost_idx])
                        
        return dp_table[n][k]
