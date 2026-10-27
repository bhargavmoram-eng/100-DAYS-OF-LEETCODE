class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = []
        
        # The first row is entirely made of free cells '.'
        grid.append("." * n)
        
        # All subsequent rows have obstacles '#' up to the last column, which is '.'
        for i in range(1, m):
            grid.append("#" * (n - 1) + ".")
            
        return grid
