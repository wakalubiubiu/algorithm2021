from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        order = []

        def recursion(nums, used=None):
            if not used:
                used = []
            if len(nums) == 0:
                result.append(order[:])
                return
            for i, e in enumerate(nums):
                if nums[i] in used:
                    continue
                order.append(e)
                del nums[i]
                recursion(nums, [])
                nums.insert(i, e)
                order.pop()
                used.append(nums[i])

        recursion(nums)
        return result
