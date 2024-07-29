# Redundant Connection Problem
# https://leetcode.com/problems/redundant-connection/

class Solution:

    class Subset:
        def __init__(self, parent, rank):
            self.parent = parent
            self.rank = rank

    def findRedundantConnection(self, edges):
        nodes = len(edges)
        subsets = [self.Subset(i, 0) for i in range(nodes + 1)]

        for edge in edges:
            x = self.find(subsets, edge[0])
            y = self.find(subsets, edge[1])
            if x != y:
                self.union(subsets, x, y)
            else:
                return edge
        return []

    def find(self, subsets, i):
        if(subsets[i].parent == i):
            return i
        else:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent
        
    def union(self, subsets, x, y):
        if(subsets[y].rank < subsets[x].rank):
            subsets[y].parent = x
        elif subsets[x].rank < subsets[y].rank:
            subsets[x].parent = y
        else:
            subsets[y].parent = x
            subsets[x].rank += 1
