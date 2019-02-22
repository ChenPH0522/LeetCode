# 2019.2.21

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # initialize
        n = len(s)
        f = [1] + [0]*n
        single = set(range(1, 10))
        multi = set(range(10, 27))
        
        # update
        for i in range(1, n+1):
            if i-1>=0 and int(s[i-1:i]) in single:
                f[i] += f[i-1]
            if i-2>=0 and int(s[i-2:i]) in multi:
                f[i] += f[i-2]
                
        return f[-1]