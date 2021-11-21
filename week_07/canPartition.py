from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for i in nums:
            total += i
        if total % 2 == 1:
            return False
        sub_total = total // 2
        sub_list = [False for _ in range(0, sub_total + 1)]
        sub_list[0] = True
        for i in nums:
            for j in range(sub_total, -1, -1):
                if sub_list[j] and i + j <= sub_total:
                    sub_list[i + j] = True
        return sub_list[sub_total]
