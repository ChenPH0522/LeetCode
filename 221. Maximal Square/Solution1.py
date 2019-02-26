# 2019.2.25

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # initialize
        nr = len(matrix)
        if nr == 0:
            return 0
        nc = len(matrix[0])
        if nc == 0:
            return 0
        mx = 0
        for r in range(nr):
            matrix[r][0] = int(matrix[r][0])
            mx = max(mx, matrix[r][0])
        for c in range(nc):
            matrix[0][c] = int(matrix[0][c])
            mx = max(mx, matrix[0][c])
        
        # update
        for r in range(1, nr):
            for c in range(1, nc):
                if matrix[r][c] == '0':
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1]) + 1
                mx = max(mx, matrix[r][c])
        
        return mx * mx
                        
        