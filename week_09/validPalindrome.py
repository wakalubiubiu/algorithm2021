class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, times):
            while left < right:
                if s[left] != s[right]:
                    return times >0 and (check(left, right-1, 0) or check(left + 1, right, 0))
                left += 1
                right -= 1
            return True
        return check(0, len(s)-1,1)