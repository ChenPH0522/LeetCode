# 2019.3.5

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        
        # initialize
        mp = {i: 1 for i in p}
        l = 1
        
        # update
        for i, j in zip(p, p[1:]):
            l = l+1 if (ord(j) - ord(i)) % 26 == 1 else 1
            mp[j] = max(mp[j], l)
            
        return sum(mp.values())