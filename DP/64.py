# Minimum Path Sum Problem
# https://leetcode.com/problems/minimum-path-sum/description/


class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        # Subproblems
        # P(n, k) - koszt dojścia do n-tego wiersza i k-tej kolumny
        # P(n, k) = min{P(n, k-1), P(n-1, k)} + P(n, k)
        # P(1, 1) = min{P(1,0), P(0,1)}
        # P(0, 0) = grid[0][0]
        costs = [[0] * n for _ in range(m)]
        costs[0][0] = grid[0][0]
        for i in range(1, n): # Dla 1 wiersza jedyna opcja to przesuwanie w prawo
            costs[0][i] = costs[0][i - 1] + grid[0][i]
        for j in range(1, m): # Dla 1 kolumny jedyna opcja to przesuwanie w dół
            costs[j][0] = costs[j - 1][0] + grid[j][0]
        row_ind = 1
        col_ind = 1
        while row_ind < m:
            while col_ind < n:
                costs[row_ind][col_ind] = min(costs[row_ind][col_ind - 1], costs[row_ind - 1][col_ind]) + grid[row_ind][col_ind]
                col_ind += 1
            col_ind = 1
            row_ind += 1
        # The minimum path sum to the bottom-right corner
        return costs[m - 1][n - 1]
            