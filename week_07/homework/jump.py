from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        min_list = [10 **9 for _ in range(m)]
        min_list[0] = 0
        for i in range(0, m):
            for j in range(1, nums[i] + 1):
                if i+j <= m-1:
                    min_list[i+j] = min(min_list[i] + 1, min_list[i+j])
                if i+j == m - 1:
                    return min_list[i+j]
        return min_list[m-1]

