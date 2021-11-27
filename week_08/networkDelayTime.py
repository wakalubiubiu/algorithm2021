from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        to = [[] for _ in range(n+1)]
        weight = [[] for _ in range(n+1)]
        dist = [10**9 for i in range(n+1)]
        for i in times:
            x = i[0]
            y = i[1]
            z = i[2]
            to[x].append(y)
            weight[x].append(z)
        dist[k] = 0
        # 标记已经拓展过的点
        expand = [False for _ in range(n+1)]
        heap = []
        heapify(heap)
        heappush(heap, (0, k))
        # 此处不要写成for循环的形式，因为这里使用的是惰性删除，这样堆里的元素实际上是多于n个的，这样有部分的元素会被抛弃不适用，如果循环的次数固定为n，那么就会有部分正确的点没有进行拓展更新。
        while heap:
            tuple_node = heappop(heap)
            local = tuple_node[1]
            temp = tuple_node[0]
            if expand[local]:
                continue
            expand[local] = True
            for j, e in enumerate(to[tuple_node[1]]):
                if dist[e] > temp + weight[local][j]:
                    dist[e] = temp + weight[local][j]
                    heappush(heap, (dist[e], e))
        ans = -1
        for i in range(1, n+1):
            ans = max(dist[i], ans)
        return ans if ans != 10**9 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[1,2,1]], 2, 2))