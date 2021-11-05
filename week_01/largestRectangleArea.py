from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for h in heights:
            accumulation = 0
            while len(stack) > 0 and stack[-1][1] >= h:
                accumulation += stack[-1][0]
                max_area = max(max_area, accumulation * stack[-1][1])
                stack.pop()
            stack.append((accumulation + 1, h))
        return max_area

