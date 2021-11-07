from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def validate(m, k, day):
            count = 0
            continuity = 0
            for now_day in bloomDay:
                if now_day <= day:
                    continuity += 1
                    if continuity == k:
                        count += 1
                        continuity = 0
                else:
                    continuity = 0
            return count >= m

        left = 0
        right = 0
        for now_day in bloomDay:
            right = max(right, now_day)
        right += 1
        unsolvable = right
        while left < right:
            mid = (left+right) //2
            if validate(m, k, mid):
                right = mid
            else:
                left = mid + 1
        if right == unsolvable:
            return -1
        return right

