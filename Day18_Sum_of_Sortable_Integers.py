class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Step 1: Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        # Step 2: Validate each divisor k
        for k in divisors:
            possible = True
            
            for i in range(0, n, k):
                b_nums = nums[i : i + k]
                b_sort = sorted_nums[i : i + k]
                
                # Count drops with wrap-around
                drops = []
                for j in range(k):
                    if b_nums[j] > b_nums[(j + 1) % k]:
                        drops.append(j)
                        
                if len(drops) > 1:
                    possible = False
                    break
                elif len(drops) == 0:
                    if b_nums != b_sort:
                        possible = False
                        break
                else:
                    # Exactly 1 drop: reconstruct the rotated array
                    j = drops[0]
                    reconstructed = b_nums[j + 1 : ] + b_nums[ : j + 1]
                    if reconstructed != b_sort:
                        possible = False
                        break
            
            if possible:
                total_sum += k
                
        return total_sum
