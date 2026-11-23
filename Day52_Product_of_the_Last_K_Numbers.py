class ProductOfNumbers(object):

    def __init__(self):
        # Initialize with 1 to handle full-array product division cleanly
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            # Reset prefix list since any product including this 0 will be 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k is >= len(self.prefix), a zero was encountered in the last k elements
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
