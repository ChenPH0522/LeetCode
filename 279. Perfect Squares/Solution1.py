# 2019.2.12

class Solution(object):
    
    mp = {0: 0}
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n not in self.mp:
        
            cand = []

            i = 1
            while i*i <= n:
                cand.append( 1 + self.numSquares(n-i*i) )
                i += 1
            
            self.mp[n] = min(cand)
            
        return self.mp[n]