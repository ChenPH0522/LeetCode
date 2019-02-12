# 2019.2.12

class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        sub, res = divmod(sum(nums), 2)
        if res != 0:
            return False
        
        if max(nums) == sub:
            return True
        if max(nums) > sub:
            return False
        
        nums.sort()
        n = len(nums)
        f = [False] * (sub+1)
        f[0] = True
        
        for i in range(n):
            level = f[:]
            for j in range(sub+1):
                if f[j] and (j+nums[i] < sub+1):
                    level[j+nums[i]] = True
            f = level
                    
        return f[-1]