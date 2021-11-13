from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        result = []
        for i, e in enumerate(new_nums):
            if i>0 and e == new_nums[i-1]:
                continue
            target = -e
            m = i+ 1
            n = len(new_nums)-1
            while m < n:
                if m > i+1 and new_nums[m] == new_nums[m-1]:
                    m +=1
                    continue
                if new_nums[m] + new_nums[n] > target:
                    n -= 1
                elif new_nums[m] + new_nums[n] < target:
                    m += 1
                else:
                    result.append([e, new_nums[m], new_nums[n]])
                    m += 1
        return result
