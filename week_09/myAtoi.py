class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        n = len(s)
        # 去掉前导空格
        while index < n and s[index] == ' ':
            index += 1
        # 检查字符是正还是负
        sign = 1
        if index < n and s[index] == '-':
            sign = -1
            index += 1
        elif index < n and s[index] == '+':
            sign = 1
            index += 1
        result = 0
        while index < n and '0' <= s[index] <= '9':
            now = ord(s[index]) - ord('0')
            # print(now)
            if result > (2 ** 31 - 1 - now) // 10:
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            result = result * 10 + now
            index += 1
        return result * sign
