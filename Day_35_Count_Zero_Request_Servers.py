class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        # 1. Sort the logs chronologically by their timestamps
        logs.sort(key=lambda log: log[1])
        
        # 2. Pair each query with its original index so we can place results correctly
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        active_servers = {}
        
        left = 0
        right = 0
        total_logs = len(logs)
        
        # 3. Process each query using a sliding window
        for original_idx, query_time in sorted_queries:
            # Include logs that fall into the window (log_time <= query_time)
            while right < total_logs and logs[right][1] <= query_time:
                server_id = logs[right][0]
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                right += 1
                
            # Remove logs that are too old to be in the window (log_time < query_time - x)
            while left < total_logs and logs[left][1] < query_time - x:
                server_id = logs[left][0]
                if server_id in active_servers:
                    active_servers[server_id] -= 1
                    if active_servers[server_id] == 0:
                        del active_servers[server_id]
                left += 1
                
            # The remaining unique keys in the dictionary received a request.
            # Total servers minus active servers gives the number of zero-request servers.
            ans[original_idx] = n - len(active_servers)
            
        return ans

        
