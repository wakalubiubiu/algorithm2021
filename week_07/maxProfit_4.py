from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 这种写法优于insert，感觉看上去更顺眼
        prices = [0] + prices
        m = len(prices)
        # 最外层的for循环要从价格为0，开始。第二层for循环是买和卖，第三层是交易的次数，这个要注意，是从0次到k次，因此此处的
        # for循环要写成k+1
        max_list = [[[-(10**9+1) for l in range(k+1)] for j in range(2)] for i in range(m)]
        max_list[0][0][0] = 0
        max_time = 0
        for i in range(1, m):
            for l in range(k+1):
                max_list[i][0][l] = max(max_list[i-1][1][l] + prices[i], max_list[i][0][l])
                if l > 0:
                    max_list[i][1][l] = max(max_list[i-1][0][l-1] - prices[i], max_list[i][1][l])
                for j in range(2):
                    max_list[i][j][l] = max(max_list[i][j][l], max_list[i-1][j][l])
        # 最后的时候可能完成0到k次之中都有可能是最佳结果，所以需要一次遍历进行循环。
        for i in max_list[m-1][0]:
            max_time = max(i, max_time)
        return max_time


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
