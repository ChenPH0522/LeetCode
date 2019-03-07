# 2019.3.6

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        n = len(nums)
        
        if k == 0:
            for l in range(n-1):
                tot = nums[l]
                for r in range(l+1, n):
                    tot += + nums[r]
                    if tot == 0:
                        return True

        if k != 0:
            for l in range(n-1):
                tot = nums[l]
                for r in range(l+1, n):
                    tot = (tot + nums[r]) % k
                    if tot == 0:
                        return True
                
        return False