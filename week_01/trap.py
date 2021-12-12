from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        stack.append((0, 0))
        relative_height = 0
        total = 0
        for i, h in enumerate(height):
            location = i+1
            if stack[-1][0] <= h:
                while len(stack) > 0 and stack[-1][0] <= h:
                    total += (stack[-1][0] - relative_height) * (location - stack[-1][1]-1)
                    relative_height = stack[-1][0]
                    stack.pop()
                if len(stack) > 0:
                    total += (h - relative_height) * (location - stack[-1][1]-1)
            relative_height = 0
            stack.append((h, location))

        return total
    """
        stack = []
        total = 0
        for h in height:
            relative_width = 0
            while len(stack) > 0 and stack[-1][1] <= h:
                bottom = stack[-1][1]
                relative_width += stack[-1][0]
                stack.pop()
                if len(stack) == 0:
                    continue
                total += relative_width * (min(h, stack[-1][1])-bottom)
            stack.append((relative_width + 1, h))
        return total
    """


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([4, 2, 0, 3, 2, 5]))
