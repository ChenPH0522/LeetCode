# 2019.3.7

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        
        self.mp = {}
        # m == 0 or n == 0
        self.helper(m, n, N, i, j)
        return self.mp[(i, j, N)]
        
        
        
    def helper(self, m, n, N, i, j):
        
        if (i, j, N) not in self.mp:
            
            if N == 0:
                self.mp[(i, j, N)] = 0
                return 0
            
            # up
            up = 1
            if i-1 >= 0:
                up = self.helper(m, n, N-1, i-1, j)

            # down
            down = 1
            if i+1 < m:
                down = self.helper(m, n, N-1, i+1, j)
            
            # left
            left = 1
            if j-1 >= 0:
                left = self.helper(m, n, N-1, i, j-1)
            
            # right
            right = 1
            if j+1 < n:
                right = self.helper(m, n, N-1, i, j+1)
            
            self.mp[(i, j, N)] = (up+down+left+right) % (10**9 + 7)
            
        return self.mp[(i, j, N)]