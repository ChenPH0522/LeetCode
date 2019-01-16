# 2018.11

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # brute force
        
        n = len(nums)
        
        for l in range(n):
            for r in range(l+1, n):
                if nums[l] + nums[r] == target:
                    return [l, r]