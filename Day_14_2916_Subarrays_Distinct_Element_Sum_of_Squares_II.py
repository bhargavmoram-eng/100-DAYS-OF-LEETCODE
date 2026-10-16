class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        
        # Segment tree arrays (4 * n size is sufficient)
        tree_sum_val = [0] * (4 * n)
        tree_sum_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def update(node, start, end, l, r, val):
            # Apply lazy updates if any exist
            if lazy[node] != 0:
                add = lazy[node]
                lazy[node] = 0
                length = end - start + 1
                tree_sum_sq[node] = (tree_sum_sq[node] + 2 * add * tree_sum_val[node] + add * add * length) % MOD
                tree_sum_val[node] = (tree_sum_val[node] + add * length) % MOD
                if start != end:
                    lazy[2 * node + 1] += add
                    lazy[2 * node + 2] += add

            # Out of bounds
            if start > r or end < l:
                return

            # Total overlap
            if l <= start and end <= r:
                length = end - start + 1
                tree_sum_sq[node] = (tree_sum_sq[node] + 2 * val * tree_sum_val[node] + val * val * length) % MOD
                tree_sum_val[node] = (tree_sum_val[node] + val * length) % MOD
                if start != end:
                    lazy[2 * node + 1] += val
                    lazy[2 * node + 2] += val
                return

            # Partial overlap
            mid = (start + end) // 2
            update(2 * node + 1, start, mid, l, r, val)
            update(2 * node + 2, mid + 1, end, l, r, val)
            
            tree_sum_val[node] = (tree_sum_val[2 * node + 1] + tree_sum_val[2 * node + 2]) % MOD
            tree_sum_sq[node] = (tree_sum_sq[2 * node + 1] + tree_sum_sq[2 * node + 2]) % MOD

        ans = 0
        last_pos = {}
        
        for j, v in enumerate(nums):
            l = last_pos.get(v, -1) + 1
            # Increment the distinct counts for all valid starting positions
            update(0, 0, n - 1, l, j, 1)
            # tree_sum_sq[0] always stores the global sum of squares
            ans = (ans + tree_sum_sq[0]) % MOD
            last_pos[v] = j
            
        return ans
