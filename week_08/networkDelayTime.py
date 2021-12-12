from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        to = [[] for _ in range(n + 1)]
        weight = [[] for _ in range(n + 1)]
        dist = [10 ** 9 for i in range(n + 1)]
        # 先标记每条边可以到大的边和权重，使用出边数组的方式。
        for i in times:
            x = i[0]
            y = i[1]
            z = i[2]
            to[x].append(y)
            weight[x].append(z)
        dist[k] = 0
        # 标记已经拓展过的点
        expand = [False for _ in range(n + 1)]
        # 循环n次，每次找一个未被标记的最小点，然后更新该点所能到达的所有出边的dist。
        for i in range(1, n):
            temp = 10 ** 9
            local = 0
            # 找dist中值最小的点切未被标记
            for j in range(1, n + 1):
                if dist[j] < temp and expand[j] == False:
                    temp = dist[j]
                    local = j
            # 标记找到的最小的点
            expand[local] = True
            # 循环更新找到的最小的点所能到达的所有出边。
            for j, e in enumerate(to[local]):
                if dist[e] > weight[local][j] + temp:
                    dist[e] = weight[local][j] + temp
            print(dist)

        ans = -1
        for i in range(1, n + 1):
            ans = max(dist[i], ans)
        return ans if ans != 10 ** 9 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

