from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prices.insert(0,0)
        max_list = [[-(10**9) for _ in range(2)] for p in prices]
        max_list[0][0] = 0
        for i in range(1, len(prices)):
            max_list[i][0] = max_list[i-1][1] + prices[i]
            # 此处在买入的时候需要手续费,加在这里
            max_list[i][1] = max_list[i-1][0] - prices[i]- fee
            for j in range(0,2):
                max_list[i][j] = max(max_list[i][j], max_list[i-1][j])
        # print(max_list)
        return max_list[len(prices)-1][0]