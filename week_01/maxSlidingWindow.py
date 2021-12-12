from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ans = []
        for i, num in enumerate(nums):
            while len(queue) > 0 and queue[0] == i - k:
                del queue[0]
            while len(queue) > 0 and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                ans.append(nums[queue[0]])
        return ans
