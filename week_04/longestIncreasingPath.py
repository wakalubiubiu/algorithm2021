from typing import List


class Solution:
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     # 网格类问题常用技巧，方向数组，遍历四个方向找到坐标或在数组中的位置
    #     dx = [-1, 0, 1, 0]
    #     dy = [0, 1, 0, -1]
    #     queue = []
    #     max_depth = 1
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     # 出边数组的建立方式
    #     to = [[] for _ in range(m * n)]
    #     degree = [0 for _ in range(m * n)]
    #     depth = [1 for _ in range(m * n)]
    #     for i, sub_list in enumerate(matrix):
    #         for j, e in enumerate(sub_list):
    #             for direction in range(4):
    #                 new_x = i + dx[direction]
    #                 new_y = j + dy[direction]
    #                 if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or matrix[new_x][new_y] <= e:
    #                     continue
    #                 # 出边数组的使用技巧，利用行x列的方式，转换为1维。
    #                 to[i*n +j].append(new_x * n +new_y)
    #                 degree[new_x * n +new_y] += 1
    #     for i, e in enumerate(degree):
    #         if e == 0:
    #             queue.append(i)
    #     while len(queue) > 0:
    #         node = queue[0]
    #         del queue[0]
    #         for location in to[node]:
    #             degree[location] -= 1
    #             # 此处用max来判断到达该点时所走过的最大深度，但是我自己写的时候发现了一个问题，就是如果能到这个点的点有
    #             # 多个的话，那么最长的路径一定是在最后到达的，所以应该不需要判断比较最大路径，而是直接记录最后到达的路径的长度就行
    #             # depth[location] = max(depth[location], depth[node] + 1)
    #             if degree[location] == 0:
    #                 queue.append(location)
    #                 depth[location] = depth[node] + 1
    #
    #     for i in depth:
    #         max_depth = max(max_depth, i)
    #
    #     return max_depth

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        m = len(matrix)
        n = len(matrix[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0

        def dfs(x, y):
            if dist[x][y] != 0:
                return dist[x][y]
            dist[x][y] = 1
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or matrix[new_x][new_y] <= matrix[x][y]:
                    continue
                dist[x][y] = max(dist[x][y], dfs(new_x, new_y) + 1)
            return dist[x][y]

        for i, sub_list in enumerate(matrix):
            for j, e in enumerate(sub_list):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
