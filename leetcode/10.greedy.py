# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """        

        print(str(s)+", "+str(p))
        
        if len(p) == 0:
            print(" * len(p) == 0")
            return False
        elif len(s) > len(p):
            return False
        elif len(s) == 0 and len(p) == 1:
            return False
        if len(s) == 1 and len(p) == 1:
            print(" * s[0] == p[0] or p[0] == '.'")
            return s[0] == p[0] or p[0] == "."
        elif p[1] == "*":
            print(" * p[1] == '*'")
            if len(s) == 0:
                return self.isMatch(s, p[2:])
            while s[0] == p[0] and len(s) > 1:
                s = s[1:]

            if p[2:] == "":
                return True

            if s[0] == p[0]:
                return self.isMatch(s[1:], p[2:])
            else:
                return self.isMatch(s, p[2:])
        return self.isMatch(s[1:], p[1:])
        
        # if len(s) > 1 and s[1] == "*":
            
        # if s[0] == p[0] and :
        #     return 
        # for i in range(len(s) - 1):
        #     for j in range(len(p) - 1):
        #         print(str(s[i])+ " - " + str(s[i]))
        #         if s[i] == ".":
        #         if s[i] == ".":
                    

s = Solution()
assert s.isMatch("aa","a") == False
assert s.isMatch("aa","aa") == True
assert s.isMatch("aaa","aa") == False
assert s.isMatch("aaa","aa") == False
assert s.isMatch("aa", "a*") == True
assert s.isMatch("aa", ".*") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aab", "c*a*b") == True
assert s.isMatch("aaa", "aaaa") == False
assert s.isMatch("aaa", "ab*a*c*a") == False
