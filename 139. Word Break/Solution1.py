# 2019.2.22

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # initialize
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        
        # update
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                f[i] = f[i] or (f[j] and (s[j:i] in wordDict))
                
        return f[-1]