# 2019.2.27

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # initialize
        f = [1]
        i2 = i3 = i5 = 0
        
        # update
        for _ in range(1, n):
            while f[i2] * 2 <= f[-1]: i2 += 1
            while f[i3] * 3 <= f[-1]: i3 += 1
            while f[i5] * 5 <= f[-1]: i5 += 1
            f.append( min(f[i2]*2, f[i3]*3, f[i5]*5) )
            
        return f[-1]