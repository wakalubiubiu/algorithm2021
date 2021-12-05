from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dx = [-1, -1, 0, 1, 1, 1, 0 ,-1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        queue_front = []
        queue_end = []
        if grid[0][0] != 0:
            return -1
        if 0 == m-1 and 0 == n-1:
            return 1
        if grid[m-1][n-1] != 0:
            return -1
        # 初始值是第一个点
        queue_front.append((0,0))
        # 初始值是最后一个点
        queue_end.append((m-1,n-1))
        visited_front = dict()
        visited_front[(0,0)] = 1
        visited_end = dict()
        visited_end[(m-1, n-1)] = 1
        self.result = -1
        def bfs(queue, visited, visited_other):
            new_queue = []
            for node in queue:
                for direction in range(8):
                    new_x = node[0] + dx[direction]
                    new_y = node[1] + dy[direction]
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        if (new_x, new_y) not in visited:
                            if (new_x, new_y) in visited_other:
                                # print(node[0], node[1], new_x, new_y)
                                self.result = visited[(node[0], node[1])] + visited_other[(new_x, new_y)]
                                return
                            visited[(new_x, new_y)] = visited[(node[0], node[1])] + 1
                            new_queue.append((new_x, new_y))
            return new_queue

        while queue_front and queue_end:
            queue_front = bfs(queue_front, visited_front, visited_end)
            if self.result > -1:
                return self.result
            queue_end = bfs(queue_end, visited_end, visited_front)
            if self.result > -1:
                return self.result
        return -1
