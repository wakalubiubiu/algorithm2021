from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.fa = [i for i in range(len(edges) + 1)]
        self.union_set(edges[0][0], edges[0][1])
        for i in edges[1:]:
            if self.find(i[0]) == self.find(i[1]):
                return i
            self.union_set(i[0], i[1])

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
