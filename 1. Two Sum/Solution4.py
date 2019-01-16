# 2018.11

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hashmap
        dic = {}
        
        for i, n in enumerate(nums):
            dic[n] = i
            
        for i, n in enumerate(nums):
            if target - n in dic and i != dic[target-n]:
                return [i, dic[target-n]]