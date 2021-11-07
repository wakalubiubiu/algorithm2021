from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        h = []
        ans = []
        for i, num in enumerate(nums):
            heapq.heappush(h, (-num, i))
            if i-1>=k:
                while h[0][1] <= i-k:
                    heapq.heappop(h)
                ans.append(-h[0][0])
        return ans
