class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        su=0
        n=len(mat)
        j=n-1
        for i in range(n):
            su=su+mat[i][i]
            su=su+mat[i][j]
            j=j-1
        if n%2!=0:
            su=su-mat[n//2][n//2]
        return su


   
    
        