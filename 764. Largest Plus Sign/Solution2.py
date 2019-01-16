# 2019.1.16

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        
        # initialize
        banned = set( [tuple(x) for x in mines] )
        f = [[0] * N for _ in xrange(N)]
        ans = 0
        
        # update
        for r in xrange(N):
            
            # rightward
            count = 0
            for c in xrange(N):
                count = 0 if (r, c) in banned else count + 1
                f[r][c] = count
                
            # leftward
            count = 0
            for c in xrange(N-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                f[r][c] = min(f[r][c], count)
                
        for c in xrange(N):
            
            # downward
            count = 0
            for r in xrange(N):
                count = 0 if (r, c) in banned else count + 1
                f[r][c] = min(f[r][c], count)
                
            # upward
            count = 0
            for r in xrange(N-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                f[r][c] = min(f[r][c], count)
                ans = max(ans, f[r][c])
                
        return ans