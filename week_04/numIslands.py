from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        ans = 0
        row_size = len(grid)
        cols_size = len(grid[0])
        visit = dict()

        def bfs(row, cols):
            queue = [(row, cols)]
            visit[row * cols_size + cols] =1
            while len(queue) > 0:
                row = queue[0][0]
                cols = queue[0][1]
                del queue[0]
                # visit的添加如果放在这里，会导致队列重复，虽然答案没有错误，但是会让队列的执行时间变长，这样答案会超出时间限制。
                # visit[row * cols_size + cols] = 1
                for direction in range(4):
                    new_row = row + dx[direction]
                    new_cols = cols + dy[direction]
                    if new_row < 0 or new_row >= row_size or new_cols < 0 or new_cols >= cols_size:
                        continue
                    if new_row*cols_size + new_cols in visit:
                        continue
                    if grid[new_row][new_cols] == '0':
                        continue
                    queue.append((new_row, new_cols))
                    # visit应该放在这里，可以判重，这样只要加入过过队列的元素，就不会再入队，这个就是队列的判重，很重要
                    visit[new_row * cols_size + new_cols] = 1

        for i, sub_list in enumerate(grid):
            for j, element in enumerate(sub_list):
                if element == '1' and i*cols_size + j not in visit:
                    ans += 1
                    bfs(i, j)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
