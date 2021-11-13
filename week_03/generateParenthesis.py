from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        result = []
        for i in range(n):
            a = self.generateParenthesis(i)
            b = self.generateParenthesis(n-i-1)
            for a_format in a:
                for b_format in b:
                    result.append("(" + a_format + ")" + b_format)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
