# 2019.3.3

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # initialize
        n = len(nums)
        f_pos = [1] * n
        f_neg = [1] * n
        mx = 0
        
        # update
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    f_pos[i] = max(f_pos[i], f_neg[j]+1)
                elif nums[i] < nums[j]:
                    f_neg[i] = max(f_neg[i], f_pos[j]+1)
                    
            mx = max(mx, f_pos[i], f_neg[i])
        
        return mx