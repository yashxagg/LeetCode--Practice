from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            
            n = len(mat)
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j], mat[j][i] = mat[j][i] , mat[i][j]
            
            for i in range(n):
                mat[i].reverse()
        
        return False