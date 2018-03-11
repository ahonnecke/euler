class Solution:
    def isPalindrome(self, x):
        s = str(x)
        if len(s) == 1:
            return True
        if s[0] != s[-1:]:
            return False
        if len(s) > 2:
            return self.isPalindrome(s[1:-1])

        return True

s = Solution()
assert s.isPalindrome("cccd") == False
assert s.isPalindrome("babab") == True
