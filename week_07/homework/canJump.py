from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        to = [False for _ in range(m)]
        to[0] = True
        for i, e in enumerate(nums):
            if to[i]:
                for j in range(nums[i]):
                    if j+i+1<m-1:
                        to[j+i+1] = True
                    if j+i+1 == m-1:
                        return True
        return to[m-1]
