# 2019.1.16

class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # dynamic programming
        import collections

        idx = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)
        res = 0
        
        for k, v in enumerate(A):
            for j in range(k):
                i = idx.get(v - A[j], None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    res = max(res, longest[j, k])
                    
        return res