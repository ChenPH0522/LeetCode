# 2019.3.1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # initialize
        f = [float('inf')] * (amount+1)
        f[0] = 0
        
        # update
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    f[i] = min(f[i-c]+1, f[i])
        
        if f[-1] == float('inf'):
            return -1
        else:
            return f[-1]