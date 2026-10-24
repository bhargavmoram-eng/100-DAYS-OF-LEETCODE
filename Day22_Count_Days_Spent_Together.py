class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :type rtype: int
        """
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to the day index of the year (1-365)
        def date_to_day_of_year(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all dates into day-of-year integers
        alice_start = date_to_day_of_year(arriveAlice)
        alice_end = date_to_day_of_year(leaveAlice)
        bob_start = date_to_day_of_year(arriveBob)
        bob_end = date_to_day_of_year(leaveBob)
        
        # Calculate intersection of the two intervals
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        # Return total overlapping days, or 0 if they don't overlap
        return max(0, overlap_end - overlap_start + 1)
