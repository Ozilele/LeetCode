# Triangle Problem
# https://leetcode.com/problems/triangle/

class Solution:

    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        costs = [[0] * n for _ in range(n)]
        costs[0][0] = triangle[0][0]
        currSum = 0
        for j in range(1, n):
            min_sum_in_row = 1000000000000000
            for k in range(len(triangle[j - 1])): # prev row
                if k == 0: # first element of row always
                    costs[j][k] = costs[j - 1][k] + triangle[j][k]
                    print(f'First el of row {costs[j][k]}')
                else:
                    costs[j][k] = min(costs[j - 1][k - 1], costs[j - 1][k]) + triangle[j][k]
                if costs[j][k] < min_sum_in_row:
                    min_sum_in_row = costs[j][k]
                col_ind = k
            costs[j][col_ind + 1] = costs[j - 1][col_ind] + triangle[j][col_ind + 1] # skrajny ostatni el wiersza
            if costs[j][col_ind + 1] < min_sum_in_row:
                min_sum_in_row = costs[j][col_ind + 1]
            currSum = min_sum_in_row
        return currSum