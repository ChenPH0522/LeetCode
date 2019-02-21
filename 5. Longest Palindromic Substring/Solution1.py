# 2019.2.20

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # initialize
        n = len(s)
        mx = float('-inf')
        l_idx, r_idx = 0, 0
        
        # update
        for r in range(n, -1, -1):
            f_new = [0] * (n+1)
            for c in range(r+1, n+1):
                if c-r == 1:
                    cand = 1
                elif c-r == 2:
                    cand = 2*(s[r]==s[c-1])
                else:
                    cand = (s[r]==s[c-1])*(f[c-1]>0)*(2 + f[c-1])
                f_new[c] = cand
                if mx < cand:
                    mx = cand
                    l_idx, r_idx = r, c
            f = f_new
                
        return s[l_idx:r_idx]