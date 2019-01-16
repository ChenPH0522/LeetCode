# 2018.11

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        
        # count
        for i, n in enumerate(nums):
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
                
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                if diff != n or dic[n] > 1:
                    n1, n2 = n, diff
                    break
        
        n = len(nums)
        
        for i in range(n):
            if nums[i] == n1:
                idx1 = i
                break
                
        for j in range(n-1, -1, -1):
            if nums[j] == n2:
                idx2 = j
                break
                
        return [idx1, idx2]