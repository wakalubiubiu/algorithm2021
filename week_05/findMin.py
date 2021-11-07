from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     mid = (left + right)//2
        #     if nums[mid] <= nums[len(nums)-1]:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return nums[right]

        left = 0
        right = len(nums)-1
        count = 1
        compare_num = nums[len(nums)-1]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < compare_num:
                right = mid
                count = len(nums) - right
                compare_num = nums[right]
            elif nums[mid] == compare_num:
                right -= 1
                count += 1
                compare_num = nums[len(nums)-count]
            else:
                left = mid + 1
        return nums[right]
