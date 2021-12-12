class Solution:
    def calculate(self, s: str) -> int:
        numbers = ''
        suffix_stack = []
        rpn_stack = []
        stack = []
        priority_map = {"+": 1, "*": 2, "-": 1, "/": 2, "(": 0}
        s += ' '
        need_zero = True
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):
                numbers +=char
                need_zero = False
                continue
            else:
                if numbers != '':
                    rpn_stack.append(numbers)
                    numbers = ''
            if char == ' ':
                continue
            if char == '(':
                suffix_stack.append(char)
                need_zero = True
                continue
            elif char == ')':
                while suffix_stack[-1] != '(':
                    rpn_stack.append(suffix_stack.pop())
                suffix_stack.pop()
                need_zero = False
                continue
            if char == '-' and need_zero:
                rpn_stack.append('0')
            while len(suffix_stack) > 0 and priority_map[suffix_stack[-1]] >= priority_map[char]:
                rpn_stack.append(suffix_stack.pop())
            need_zero = True
            suffix_stack.append(char)
        while len(suffix_stack) > 0:
            rpn_stack.append(suffix_stack.pop())
        for s in rpn_stack:
            if s not in ["+", "-", "*", "/"]:
                stack.append(s)
            else:
                element2 = int(stack.pop())
                element1 = int(stack.pop())
                if s == '+':
                    element = element1 + element2
                elif s == '-':
                    element = element1 - element2
                elif s == '*':
                    element = element1 * element2
                else:
                    """
                    注意负数除法的问题
                    """
                    element = int(element1 / element2)
                stack.append(element)
        return int(stack.pop())


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))