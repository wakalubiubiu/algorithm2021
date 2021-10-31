from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
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
    print(solution.evalRPN(["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/", "26", "-14", "-", "-",
                            "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+", "156", "/", "173", "/", "-24", "11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))
