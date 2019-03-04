# 2019.3.3

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n < 2:
            return n
        
        down = up = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down+1
            elif nums[i] < nums[i-1]:
                down = up+1
                
        return max(down, up)