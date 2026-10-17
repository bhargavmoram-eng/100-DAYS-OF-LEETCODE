class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        # Helper function to compute the sum of digits of a number
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        n = len(nums)
        # Pair each number with its original index: (num, original_index)
        arr = [(num, i) for i, num in enumerate(nums)]
        
        # Sort based on digit sum (ascending), then by the number itself (ascending)
        arr.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        swaps = 0
        
        # Use cycle decomposition to find the minimum number of swaps
        for i in range(n):
            # If the element is already visited or already in the correct position
            if visited[i] or arr[i][1] == i:
                continue
            
            # Calculate the size of the cycle
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][1]  # Move to the original index where this element came from
                cycle_size += 1
            
            # A cycle of size L requires L - 1 swaps to be fully sorted
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
