# 2019.2.20

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # initialize
        nr = len(obstacleGrid)
        if nr == 0:
            return 0
        nc = len(obstacleGrid[0])
        if nc == 0:
            return 0
        
        f = [ [0] * (nc) for _ in range(nr) ]
        if obstacleGrid[0][0] == 0:
            f[0][0] = 1
        else:
            f[0][0] = 0
        
        flag = obstacleGrid[0][0]
        for r in range(1, nr):
            if (not flag) and (obstacleGrid[r][0] != 1):
                f[r][0] = 1
            else:
                flag = 1
                f[r][0] = 0
                
        flag = obstacleGrid[0][0]
        for c in range(1, nc):
            if (not flag) and (obstacleGrid[0][c] != 1):
                f[0][c] = 1
            else:
                flag = 1
                f[0][c] = 0
                
        # update
        for r in range(1, nr):
            for c in range(1, nc):
                if obstacleGrid[r][c] == 1:
                    f[r][c] = 0
                else:
                    f[r][c] = f[r-1][c] + f[r][c-1]
        
        return f[-1][-1]