# 2019.2.13

class Solution(object):
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # initialize
        f = [[0] * (n+1) for _ in range(m+1)]
        
        # update
        for s in strs:
            n0 = s.count('0')
            n1 = s.count('1')
            
            for i in range(m, n0-1, -1):
                for j in range(n, n1-1, -1):
                    f[i][j] = max(f[i][j], f[i-n0][j-n1] + 1)
                    
        return f[-1][-1]