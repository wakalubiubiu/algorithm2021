from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        result = [[0 for j in range(2)] for i in range(m + 1)]
        for i in range(1, m + 1):
            result[i][0] = max(result[i - 1][1], result[i - 1][0])
            result[i][1] = result[i - 1][0] + nums[i - 1]
        print(result)
        return max(result[m][0], result[m][1])

