# 2019.2.14

class Solution(object):
        
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N == 1:
            return 10
        
        # initialize
        mp = {}
        lst = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        for n in lst:
            mp[n] = 1
            
        # update
        for _ in range(N-1):
            mp_new = {}
            for i in mp:
                tot = 0
                for k in self.nextNumber(i):
                    tot += mp[k]
                mp_new[i] = tot
            mp = mp_new
        
        return sum(mp.values()) % (10**9 + 7)
        
        
    
    def nextNumber(self, n):
        
        if n == 1:
            return (6, 8)
        if n == 2:
            return (7, 9)
        if n == 3:
            return (4, 8)
        if n == 4:
            return (3, 9, 0)
        if n == 6:
            return (1, 7, 0)
        if n == 7:
            return (2, 6)
        if n == 8:
            return (1, 3)
        if n == 9:
            return (2, 4)
        if n == 0:
            return (4, 6)