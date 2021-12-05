class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        len_palindrome = 0
        start = 0
        for i in range(n):
            left = i - 1
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len_palindrome:
                start = left + 1
                len_palindrome = right - left - 1

        for i in range(1, n):
            left = i - 1
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len_palindrome:
                start = left + 1
                len_palindrome = right - left - 1
        return s[start: start + len_palindrome]
