class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # initialize
        n = len(nums)
        if n == 0:
            return 0
        mx = mn = res = nums[0]
        
        # update
        for i in range(1, n):
            if nums[i] > 0:
                mx, mn = max(mx*nums[i], nums[i]), min(mn*nums[i], nums[i])
            elif nums[i] == 0:
                mx = mn = 0
            else:
                mx, mn = max(mn*nums[i], nums[i]), min(mx*nums[i], nums[i])
            res = max(res, mx)
                
        return res
        