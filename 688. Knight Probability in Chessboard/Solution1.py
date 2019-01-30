# 2019.1.29

class Solution:
    
    
    
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        self.map = {}
        return self.helper(N, K, r, c)
        
        
    def helper(self, N, K, r, c):
                
        if (r<0) or (r>N-1) or (c<0) or (c>N-1):
            return 0
        
        if K == 0:
            return 1
        
        if (r, c, K) not in self.map:
            
            # up-left
            u1 = self.helper(N, K-1, r-2, c-1)
            
            # up-right
            u2 = self.helper(N, K-1, r-2, c+1)
            
            # down-left
            d1 = self.helper(N, K-1, r+2, c-1)
            
            # down-right
            d2 = self.helper(N, K-1, r+2, c+1)
            
            # left-up
            l1 = self.helper(N, K-1, r-1, c-2)
            
            # left-down
            l2 = self.helper(N, K-1, r+1, c-2)
            
            # right-up
            r1 = self.helper(N, K-1, r-1, c+2)
            
            # right-down
            r2 = self.helper(N, K-1, r+1, c+2)
            
            self.map[(r, c, K)] = (u1+u2+d1+d2+l1+l2+r1+r2)/8
            
        return self.map[(r, c, K)]
            
        