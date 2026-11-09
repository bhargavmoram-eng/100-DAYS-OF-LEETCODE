import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        # Count requests handled by each server
        requests_count = [0] * k
        
        # Track available/idle servers in sorted order
        available = SortedList(range(k))
        
        # Min-heap to track busy servers: (end_time, server_id)
        busy_heap = []
        
        for i, current_time in enumerate(arrival):
            # 1. Free up servers that finished before or at current arrival time
            while busy_heap and busy_heap[0][0] <= current_time:
                _, server_id = heapq.heappop(busy_heap)
                available.add(server_id)
            
            # If all servers are busy, the request is dropped
            if not available:
                continue
                
            # 2. Find the preferred server using modular arithmetic
            preferred = i % k
            
            # Find the first available server index >= preferred
            idx = available.bisect_left(preferred)
            
            # If no server >= preferred exists, wrap around to the beginning (0)
            if idx == len(available):
                idx = 0
                
            chosen_server = available.pop(idx)
            
            # 3. Assign the request to the server
            requests_count[chosen_server] += 1
            heapq.heappush(busy_heap, (current_time + load[i], chosen_server))
            
        # Find the max requests handled by any server
        max_requests = max(requests_count)
        
        # Collect all servers that achieved the maximum count
        return [i for i, count in enumerate(requests_count) if count == max_requests]
