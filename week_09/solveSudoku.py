from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 此处维护是每一行，每一列、每一个小方块可以填的数字都是什么
        row_result = [[True] * 10 for _ in range(9)]
        col_result = [[True] * 10 for _ in range(9)]
        board_result = [[True] * 10 for _ in range(9)]
        for i, sub in enumerate(board):
            for j, e in enumerate(sub):
                if e != '.':
                    digital = ord(e) - ord('0')
                    row_result[i][digital] = False
                    col_result[j][digital] = False
                    board_result[(i // 3) * 3 + j // 3][digital] = False

        def dfs():
            pos = find_min_available()
            x = pos[0]
            y = pos[1]
            if x == -1:
                return True
            result = find_available(x, y)
            for i in result:
                row_result[x][i] = False
                col_result[y][i] = False
                board_result[(x // 3) * 3 + y // 3][i] = False
                board[x][y] = str(i)
                if dfs():
                    return True
                row_result[x][i] = True
                col_result[y][i] = True
                board_result[(x // 3) * 3 + y // 3][i] = True
                board[x][y] = '.'
            return False

        def find_min_available():
            min_available = 10
            pos = [-1, -1]
            # 这个地方写错了，应该返回的是坐标，所以循环，应该是0~9，不是1~10
            for i in range(0, 9):
                for j in range(0, 9):
                    # 此处加上这个才可能返回-1，因为如果已经填满了，所有格子都不是'.'。
                    if board[i][j] != '.':
                        continue
                    result = find_available(i, j)
                    if len(result) < min_available:
                        min_available = len(result)
                        pos = [i, j]
            return pos

        def find_available(i: int, j: int) -> List[int]:
            result = []
            for k in range(1, 10):
                if row_result[i][k] and col_result[j][k] and board_result[(i // 3) * 3 + j // 3][k]:
                    result.append(k)
            return result

        dfs()