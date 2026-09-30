class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        su=0
        n=len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    su=su+mat[i][j]
                elif i+j==n-1:
                    su=su+mat[i][j]
        return su
        
        