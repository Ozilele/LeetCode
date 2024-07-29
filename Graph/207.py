# Course Schedule Problem
# https://leetcode.com/problems/course-schedule/description/

class Solution:

    def canFinish(self, numCourses: int, list) -> bool:
        n = len(list)
        graph = [[] for _ in range(numCourses)]
        # finding if this graph has a cycle
        for x, y in list:
            graph[x].append(y)
        print(graph)
        # visited = [False] * numCourses
        visited = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True

    def dfs(self, v, visited, graph): # visited[v] = 0 -> node has not been visited
        if visited[v] == -1: # case when there is a cycle in graph - false ret
            return False
        if visited[v] == 1:
            return True
        visited[v] = -1 # node is being visited
        for elem in graph[v]:
            if not self.dfs(elem, visited, graph):
                return False
        visited[v] = 1 # node has been visited
        return True
