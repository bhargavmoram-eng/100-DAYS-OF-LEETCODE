class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        max_factor = max(factor for factor, _ in items)
        
        # Step 1: Count occurrences of each factor
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # Step 2: Count total items whose factor is divisible by f
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[multiple]
                    
        # Step 3: Sort items by price ascending
        items.sort(key=lambda x: x[1])
        min_price = items[0][1]
        
        total_items = 0
        
        # Step 4: Greedily buy "doubles" (1 bought + 1 free) while cost < 2 * min_price
        for factor, price in items:
            if price >= 2 * min_price:
                break
                
            # Number of other items this item can grant for free
            free_capacity = multiples_count[factor] - 1
            if free_capacity <= 0:
                continue
                
            # Buy as many doubles as capacity and budget allow
            can_buy = min(free_capacity, budget // price)
            total_items += can_buy * 2
            budget -= can_buy * price
            
        # Step 5: Spend remaining budget on the cheapest item (1 item per purchase)
        total_items += budget // min_price
        
        return total_items
