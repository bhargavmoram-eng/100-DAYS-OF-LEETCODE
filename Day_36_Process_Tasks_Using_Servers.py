import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # Min-heap for free servers: (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # Min-heap for busy servers: (free_time, weight, index)
        used_servers = []
        
        ans = []
        t = 0
        
        for j, task_time in enumerate(tasks):
            # Advance time to at least the arrival time of the current task
            t = max(t, j)
            
            # If no servers are free, fast-forward time to when the first server becomes available
            if not free_servers:
                t = used_servers[0][0]
                
            # Release all servers that have finished their tasks by the current time t
            while used_servers and used_servers[0][0] <= t:
                time_free, weight, idx = heapq.heappop(used_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            # Assign the current task to the best available free server
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            
            # Put the server into the busy heap with its updated completion time
            heapq.heappush(used_servers, (t + task_time, weight, idx))
            
        return ans
