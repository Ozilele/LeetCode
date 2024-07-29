# Number of Provinces Problem
# https://leetcode.com/problems/number-of-provinces/

from queue import Queue

class Solution:

    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        print(adj)
        visited = [False] * len(adj)
        provinces = 0

        for i in range(len(adj)):
            if adj[i] == []: # element i is single province
                provinces += 1
            else: # element has some directed provinces
                if visited[i] is False:
                    cities = []
                    self.dfs(i, visited, adj, cities)
                    print(cities)
                    provinces += 1
        return provinces

    def dfs(self, v, visited, adj, arr):
        visited[v] = True
        arr.append(v)
        for neigh in adj[v]:
            if visited[neigh] is False:
                self.dfs(neigh, visited, adj, arr)
