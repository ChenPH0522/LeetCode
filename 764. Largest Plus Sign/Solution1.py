# 2019.1.16
# TimeLimitExceeded

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        
        # brute force
        banned = set( [tuple(x) for x in mines] )
        ans = 0
        
        for r in range(N):
            for c in range(N):
                k = 0
                while ((r-k >= 0) and (r+k < N) and
                    (c-k >= 0) and (c+k < N) and
                    (r-k, c) not in banned and
                    (r+k, c) not in banned and
                    (r, c-k) not in banned and
                    (r, c+k) not in banned):
                    k += 1
                ans = max(ans, k)
                
        return ans