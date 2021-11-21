from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_sum = [[0 for i in sub] for sub in triangle]
        min_sum[0][0] = triangle[0][0]
        min_total = 10 ** 4 + 1
        for i, sub in enumerate(triangle[1:]):
            for j, e in enumerate(sub):
                # 最左侧的点只和它上一层最左侧的点相关，因此可以直接相加
                if j == 0:
                    min_sum[i + 1][j] = min_sum[i][j] + e
                # 最右侧的点同理，也可以直接相加
                elif j == len(sub) - 1:
                    min_sum[i + 1][j] = min_sum[i][j - 1] + e
                # 中间的点的最小路径取决于上一层可以到达该点的两个点，取其中的最小值即为当前点的最小值。
                else:
                    min_sum[i + 1][j] = min(min_sum[i][j - 1], min_sum[i][j]) + e

        for i in min_sum[len(min_sum) - 1]:
            min_total = min(min_total, i)
        return min_total


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[10000], [10000, 10000], [10000, 10000, 10000]]))
