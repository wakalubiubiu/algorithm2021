from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        edges = []
        # 并查集建立初始化每个集合的根都是它自己
        fa = [i for i in range(m)]

        def find(x):
            if x == fa[x]:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        for i in range(0, m):
            for j in range(i+1, m):
                edges.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1]- points[j][1])])

        edges_sorted = sorted(edges, key=lambda x: x[2])
        ans = 0
        for edge in edges_sorted:
            # 此处就是于并查集的合并同时加了一个求和操作
            x = find(edge[0])
            y = find(edge[1])
            if x != y:
                ans += edge[2]
                fa[x] = y

        return ans
