from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum_pre = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # for循环的边界值是m+1，n+1 不要弄错了，如果写m的话，那么m行就没计算了。
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sum_pre[i][j] = self.sum_pre[i][j-1] + self.sum_pre[i-1][j] - self.sum_pre[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.sum_pre[row2][col2] -self.sum_pre[row2][col1-1] - self.sum_pre[row1-1][col2] + self.sum_pre[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    num_matrix = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    num_matrix.sumRegion(1,1,2,2)