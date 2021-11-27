from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[10 ** 9] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]
            dist[x][y] = dist[y][x] = z

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        min_neighbour = 10 ** 9
        ans = 0
        for i in range(n):
            neighbour = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    neighbour += 1
            if neighbour <= min_neighbour:
                ans = i
                min_neighbour = neighbour
        return ans
