from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        shagnse = True
        visited = [[0 for _ in range(len(sub_list))] for sub_list in board]

        now_visited = [[0 for _ in range(len(sub_list))] for sub_list in board]

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def dfs(i, j):
            # print(i,j)
            nonlocal shagnse
            queue = []
            queue.append([i, j])
            now_visited[i][j] = 1
            while len(queue) > 0:
                node = queue[0]
                del queue[0]
                for direction in range(4):
                    new_x = node[0] + dx[direction]
                    new_y = node[1] + dy[direction]
                    if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or board[new_x][new_y] == 'X':
                        continue
                    if visited[new_x][new_y] != 0 or now_visited[new_x][new_y] != 0:
                        continue
                    if new_x == m - 1 or new_y == n - 1:
                        shangse = False
                    # print(new_x, new_y)
                    queue.append([new_x, new_y])
                    now_visited[new_x][new_y] = 1

        for i, sub_list in enumerate(board):
            for j, e in enumerate(sub_list):
                if visited[i][j] == 0 and e != 'X':
                    print(i, j, board[i][j], e)
                    dfs(i, j)
                    value = 1 if shagnse else 2
                    for i1, sub_list1 in enumerate(now_visited):
                        for j1, e1 in enumerate(sub_list1):
                            # print(i,j, e)
                            if e1 == 1:
                                # print(i,j,value)
                                visited[i1][j1] = value
                            now_visited[i1][j1] = 0

        for i, sub_list in enumerate(board):
            for j, e in enumerate(sub_list):
                if visited[i][j] == 1:
                    board[i][j] = 'X'


if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))