# 2019.3.13

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # initialize
        n = len(nums)
        f = [ [1, 1] for _ in range(n) ]
        max_len = 1
        
        # update
        for i, num in enumerate(nums):
            
            count = 0
            
            for j in range(i):
                f[i][0] = max( f[i][0], (f[j][0]+1) * (num>nums[j]) )
            
            for j in range(i):
                count += f[j][1] * (f[i][0]-f[j][0]==1) * (nums[j]<num)
            
            f[i] = [ f[i][0], max(f[i][1], count) ]
            max_len = max( max_len, f[i][0] )

        count = 0
        for i in range(n):
            count += (f[i][0] == max_len) * f[i][1]
            
        return count