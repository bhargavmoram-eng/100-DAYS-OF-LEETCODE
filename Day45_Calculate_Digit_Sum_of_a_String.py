class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = []
            # Iterate through the string in steps of size k
            for i in range(0, len(s), k):
                group = s[i : i + k]
                # Calculate the sum of digits in the current group
                group_sum = sum(int(digit) for digit in group)
                new_s.append(str(group_sum))
            
            # Merge the groups into the updated string for the next round
            s = "".join(new_s)
            
        return s
