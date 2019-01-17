# 2019.1.17


class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        
        # initialize
        nA = len(A)
        cumA = [0] * (nA+1)
        tot = 0
        for i in range(1, nA+1):
            tot += A[i-1]
            cumA[i] = tot
        
        f = [ [0] * (nA+1) for _ in range(K+1) ]
        for c in range(1, nA+1):
            f[1][c] = cumA[c] / c
        
        # update
        for r in range(2, K+1):
            for c in range(r, nA+1):
                for j in range(r-1, c):
                    f[r][c] = max(f[r][c], f[r-1][j] + (cumA[c] - cumA[j])/(c-j))
                    
        return f[-1][-1]