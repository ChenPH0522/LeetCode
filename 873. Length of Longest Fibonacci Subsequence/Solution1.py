# 2019.1.16

class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # brute force
        s = set(A)
        ans, nA = 0, len(A)
        
        for i in range(nA):
            for j in range(i+1, nA):
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in s:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
                
        return ans if ans >= 3 else 0