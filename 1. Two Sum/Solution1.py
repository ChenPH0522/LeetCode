# 2018.12

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            else:
                dic[ target - n ] = i
        