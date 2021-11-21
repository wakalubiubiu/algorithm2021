from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # min_list = [10**9 for _ in range(n+1)]
        # min_list[0] = 0
        # for i in range(1, n+1):
        #     for j in range(1, int(sqrt(n))+1):
        #         min_list[i] = min(min_list[i], min_list[i-j*j]+1)
        # return min_list[n]

        min_list = [10 ** 9 for _ in range(n + 1)]
        min_list[0] = 0
        for i in range(1, int(sqrt(n)) + 1):
            for j in range(i * i, n + 1):
                min_list[j] = min(min_list[j], min_list[j - i * i] + 1)
        return min_list[n]
