# 2019.2.11

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        # initialize
        n = len(days)
        f = [0] * (n+1)
        f[-2] = min(costs)
        
        # update
        for i in range(n-2, -1, -1):
            
            j = i+1
            c1 = costs[0] + f[j]
            
            while j < n and days[j] - days[i] <= 6:
                j += 1
            c2 = costs[1] + f[j]
            
            while j < n and days[j] - days[i] <= 29:
                j += 1
            c3 = costs[2] + f[j]
            
            f[i] = min(c1, c2, c3)
            
        return f[0]