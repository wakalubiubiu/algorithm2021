class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = False
        for letter in s:
            if letter in ('[', '(', '{'):
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                element = stack.pop()
                if letter == ']' and element != '[':
                    return False
                elif letter == '}' and element != '{':
                    return False
                elif letter == ')' and element != '(':
                    return False
        return not (len(stack)>0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("([]){"))
