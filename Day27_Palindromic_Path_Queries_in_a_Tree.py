class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Iterative DFS for Euler Tour and Binary Lifting Setup
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        
        LOG = 20  # Safe upper bound for n <= 10^5
        up = [[0] * LOG for _ in range(n)]
        
        # Iterative DFS using a stack to avoid recursion limit and nonlocal keyword
        stack = [(0, 0, 0, 0)] # (node, parent, d, state: 0 for entry, 1 for exit)
        timer = 0
        
        while stack:
            node, parent, d, state = stack.pop()
            if state == 0:
                timer += 1
                tin[node] = timer
                depth[node] = d
                up[node][0] = parent
                
                for i in range(1, LOG):
                    up[node][i] = up[up[node][i-1]][i-1]
                
                # Push exit state first, then children entry states
                stack.append((node, parent, d, 1))
                for neighbor in adj[node]:
                    if neighbor != parent:
                        stack.append((neighbor, node, d + 1, 0))
            else:
                tout[node] = timer

        # LCA Helper function using binary lifting
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # 3. Fenwick Tree (Binary Indexed Tree) for range XOR updates
        bit = [0] * (timer + 2)
        
        def bit_update(idx, val):
            while idx <= timer:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def range_xor(l, r, val):
            bit_update(l, val)
            bit_update(r + 1, val)

        # Initialize the tree masks with the initial string characters
        current_chars = list(s)
        for i in range(n):
            char_mask = 1 << (ord(current_chars[i]) - ord('a'))
            range_xor(tin[i], tout[i], char_mask)
            
        # 4. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = current_chars[u]
                
                if old_c != new_c:
                    change_mask = (1 << (ord(old_c) - ord('a'))) ^ (1 << (ord(new_c) - ord('a')))
                    range_xor(tin[u], tout[u], change_mask)
                    current_chars[u] = new_c
                    
            elif parts[0] == "query":
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                mask_lca_node = 1 << (ord(current_chars[lca]) - ord('a'))
                
                path_mask = mask_u ^ mask_v ^ mask_lca_node
                
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans
