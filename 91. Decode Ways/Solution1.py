# 2019.2.21

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # initialize
        n = len(s)
        if n == 0: return 0
        if int(s[0]) == 0: return 0
        
        f2, f1 = 1, 1
        
        # update
        for i in range(1, n):
            
            if int(s[i-1:i+1]) == 0:
                return 0
            
            if int(s[i-1:i+1]) == 10 or int(s[i-1:i+1]) == 20:
                f2, f1 = f1, f2
                continue
            
            if int(s[i-1:i+1]) <= 9:
                f2, f1 = f1, f1
                continue
            
            if int(s[i-1:i+1]) <= 26:
                f2, f1 = f1, f2+f1
                continue
                
            if int(s[i-1:i+1]) > 26 and int(s[i-1:i+1])%10 == 0:
                return 0
            
            if int(s[i-1:i+1]) > 26:
                f2, f1 = f1, f1
                continue
            
        return f1