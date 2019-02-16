# 2019.2.15

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # initialize
        f = [[0] * (n+2) for _ in range(n+2)]
        
        # update
        for r in range(n-1, 0, -1):
            for c in range(r+1, n+1):
                f[r][c] = float('inf')
                for k in range(r-1, c+1):
                    cand = k + max(f[r][k-1], f[k+1][c])
                    f[r][c] = min(f[r][c], cand)
        
        return f[1][n]