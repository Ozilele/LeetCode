# All Paths From Source to Target Problem
# https://leetcode.com/problems/all-paths-from-source-to-target/description/

from queue import Queue

class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        visited = [False] * n
        # self.paths = [[] for _ in range(n)]
        self.paths = []
        self.currPath = []
        self.runModifiedDfs(0, graph, visited)
        return self.paths

    def runModifiedDfs(self, v, graph, visited):
        visited[v] = True
        self.currPath.append(v)
        if v == len(graph) - 1: # last vertice
            self.paths.append(self.currPath.copy())  # Save a copy of the current path
            for node in self.currPath:
                if node != 0:
                    visited[node] = False
        else:
            for node in graph[v]:
                if visited[node] is False:
                    self.runModifiedDfs(node, graph, visited)
        self.currPath.pop() # Backtrack to apply good solution



