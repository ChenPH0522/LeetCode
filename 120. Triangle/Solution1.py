# 2019.2.13

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # initialize
        n = len(triangle)
        if n == 0:
            return 0
        n_k = len(triangle[-1])
        prev = [0] * (n_k + 1)
        
        # update
        for arr in triangle[::-1]:
            
            for i, num in enumerate(arr):
                arr[i] = num + min(prev[i], prev[i+1])
            
            prev = arr
            
        return prev[0]