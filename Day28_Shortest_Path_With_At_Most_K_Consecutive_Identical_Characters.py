import heapq
from collections import defaultdict

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        # If k is less than 1, we can't even stand on the starting node validly
        if k < 1:
            return -1
            
        # Build the adjacency list for the directed graph
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][c] stores the minimum weight to reach node `u` with a 
        # consecutive identical character count of `c`
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Priority queue stores tuples of (current_total_weight, current_node, consec_count)
        # Starting at node 0, the first character has a consecutive count of 1
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, consec = heapq.heappop(pq)
            
            # Since Dijkstra processes paths in increasing order of weight,
            # the first time we reach the destination node, it is guaranteed to be optimal.
            if u == n - 1:
                return d
                
            # Skip if we found a shorter path to this specific state already
            if d > dist[u][consec]:
                continue
                
            # Traverse all directed neighbors
            for v, w in adj[u]:
                # Calculate consecutive count for the neighbor
                if labels[v] == labels[u]:
                    next_consec = consec + 1
                else:
                    next_consec = 1
                    
                # Only proceed if the consecutive constraint is satisfied
                if next_consec <= k:
                    if d + w < dist[v][next_consec]:
                        dist[v][next_consec] = d + w
                        heapq.heappush(pq, (d + w, v, next_consec))
                        
        return -1
