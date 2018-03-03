class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        substring = ""
        mymax = 1
        for i in range(len(s)):
            j = 0
            substring = ""
            for j in range(i, len(s)):
                if s[j] in substring:
                    break
                else: 
                    substring += str(s[j])
                    
                mymax = max(mymax, len(substring))
        return mymax

s = Solution()
check = "pwwkew"
check = "c"
check = "au"
print("Checking " + check)
print(str(s.lengthOfLongestSubstring(check)))
#print(str(s.lengthOfLongestSubstring('abcabcbb')))
