class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_not_digital_or_letter(sub):
            if sub < '0' or sub > '9' or sub < 'a' or sub > 'z' or sub < 'A' or sub > 'Z':
                print(sub, 22222222222222)
                return True

        def getNext(i):
            while i < len(s) and is_not_digital_or_letter(s[i]):
                i += 1
            return i

        def getPre(i):
            print(i, s[i])
            while i < len(s) and is_not_digital_or_letter(s[i]):
                print(s[i], 11111111)
                i -= 1
            return i

        def equals_ignore(i, j):
            s1 = s[i]
            s2 = s[j]
            # print(s1, s2)
            if 'A' <= s1 <= 'Z':
                s1 = chr(ord(s1) - ord('A') + ord('a'))
            if 'A' <= s2 <= 'Z':
                s2 = chr(ord(s2) - ord('A') + ord('a'))
            return s1 != s2

        left = 0
        right = len(s) - 1
        while left < right:
            # print(left, right)
            if equals_ignore(left, right):
                return False
            left = getNext(left + 1)
            right = getPre(right - 1)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.isPalindrome("A man, a plan, a canal: Panama")