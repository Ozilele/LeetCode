# Unique Paths Problem
# https://leetcode.com/problems/unique-paths/description/

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # The robot can move either down or right at any point of time
        # Path(i,j) - number of unique paths to grid[i][j]
        # Path(i,j) = Path(i-1,j) + Path(i,j-1)
        grid = [[0] * n for _ in range(m)]
        for i in range(n):
            grid[0][i] = 1
        for j in range(m):
            grid[j][0] = 1
        
        row_ind = 1
        col_ind = 1
        while row_ind < m:
            while col_ind < n:
                grid[row_ind][col_ind] = grid[row_ind - 1][col_ind] + grid[row_ind][col_ind - 1]
                col_ind += 1
            col_ind = 1
            row_ind += 1
        return grid[m - 1][n - 1]