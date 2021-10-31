class Solution:
    def calculate(self, s: str) -> int:
        numbers = ''
        suffix_stack = []
        rpn_stack = []
        stack = []
        priority_map = {"+": 1, "*": 2, "-": 1, "/": 2}
        s += ' '
        for char in s:
            if ord('0') <= ord(char) <= ord('9'):
                numbers +=char
                continue
            else:
                if numbers != '':
                    rpn_stack.append(numbers)
                    numbers = ''
            if char == ' ':
                continue
            while len(suffix_stack) >0 and priority_map[suffix_stack[-1]] >= priority_map[char]:
                rpn_stack.append(suffix_stack.pop())
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
