# 2019.3.17

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mp = self.counter(nums)
        uni = sorted( list(mp.keys()) )
        
        n = len(uni)
        if n == 0:
            return 0
        if n == 1:
            return uni[0] * mp[uni[0]]
        
        # initialize
        f0 = 0
        f1 = uni[0] * mp[uni[0]]
        
        # update
        for i in range(1, n):
            if uni[i] - uni[i-1] == 1:
                f0, f1 = max(f0, f1), f0 + uni[i] * mp[uni[i]]
            else:
                f0, f1 = max(f0, f1), max(f0, f1) + uni[i] * mp[uni[i]]
            
        return max(f0, f1)
    
    
    def counter(self, nums):
        
        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] += 1
                
        return mp