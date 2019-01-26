# 2019.1.26

class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        push = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        push = [(-1, 'L')] + push + [(len(dominoes), 'R')]
        ans = list(dominoes)
        
        for (i, x), (j, y) in zip(push, push[1:]):
            
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    a, b = k-i, j-k
                    ans[k] = '.LR'[(a>b)-(a<b)]
                    
        return ''.join(ans)