# 2019.3.4

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger+1), desiredTotal)
        
    def helper(self, nums, total):
        
        hash = tuple(nums)
        
        if hash in self.memo:
            return self.memo[hash]
        
        if nums[-1] >= total:
            self.memo[hash] = True
            return True
        
        n = len(nums)
        for i in range(n):
            if not self.helper(nums[:i] + nums[i+1:], total-nums[i]):
                self.memo[hash] = True
                return True
        
        self.memo[hash] = False
        return False