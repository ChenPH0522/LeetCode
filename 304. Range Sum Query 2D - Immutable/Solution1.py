# 2019.2.28

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        nr = len(matrix)
        if nr == 0:
            self.mat = []
            return
        nc = len(matrix[0])
        if nc == 0:
            self.mat = []
            return
        self.mat = [ [0] * nc for _ in range(nr) ]
        self.mat[0][0] = matrix[0][0]
        
        for r in range(1, nr):
            self.mat[r][0] = self.mat[r-1][0] + matrix[r][0]
        for c in range(1, nc):
            self.mat[0][c] = self.mat[0][c-1] + matrix[0][c]
        for r in range(1, nr):
            for c in range(1, nc):
                self.mat[r][c] = self.mat[r-1][c] + self.mat[r][c-1] - self.mat[r-1][c-1] + matrix[r][c]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        if row1 == 0 and col1 == 0:
            return self.mat[row2][col2]
        
        if row1 == 0:
            if row2 == 0:
                return self.mat[0][col2] - self.mat[0][col1-1]
            if row2 != 0:
                return self.mat[row2][col2] - self.mat[row2][col1-1]
        
        if col1 == 0:
            if col2 == 0:
                return self.mat[row2][0] - self.mat[row1-1][0]
            if col2 != 0:
                return self.mat[row2][col2] - self.mat[row1-1][col2]
            
        return self.mat[row2][col2] - self.mat[row2][col1-1] - self.mat[row1-1][col2] + self.mat[row1-1][col1-1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)