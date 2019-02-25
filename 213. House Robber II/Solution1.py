# 2019.2.24

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        l = self.rob1(nums, 0, n-1)
        r = self.rob1(nums, 1, n)
        return max(l, r)
        
    def rob1(self, nums, lt, rt):
        
        if rt-lt == 0:
            return 0
        if rt-lt == 1:
            return nums[lt]
        
        # dynamic programming
        f2, f1 = 0, nums[lt]
        for i in range(lt+1, rt):
            f2, f1 = f1, max(f2+nums[i], f1)
            
        return f1