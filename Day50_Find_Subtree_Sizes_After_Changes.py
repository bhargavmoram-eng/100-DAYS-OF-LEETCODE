from collections import defaultdict

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        # Tracks the closest ancestor for each character 'a'-'z'
        last_seen = {} 
        
        def dfs_reparent(u):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            # If an ancestor with the same character exists, update parent
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            # Set current node as the closest ancestor for this character
            last_seen[char] = u
            
            for v in adj[u]:
                dfs_reparent(v)
                
            # Backtrack to restore state for other branches
            last_seen[char] = prev_ancestor

        dfs_reparent(0)
        
        # Build the updated tree
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u):
            for v in new_adj[u]:
                dfs_size(v)
                ans[u] += ans[v]
                
        dfs_size(0)
        return ans
