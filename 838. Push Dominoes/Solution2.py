# 2019.1.26

class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        N = len(dominoes)
        force = [0] * N
        
        # L --> R
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f
            
        # L <-- R
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f
            
        for i, f in enumerate(force):
            if f > 0: force[i] = 'R'
            elif f == 0: force[i] = '.'
            else: force[i] = 'L'
                
        return ''.join(force)