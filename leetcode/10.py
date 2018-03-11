# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

class patChar:
    isWild = False
    isMultiple = False
    
    def isEq(char):
        return self.value == "." or char == "." or char == self.value

    def isEq(char):
        return self.value == "." or char == "." or char == self.value
        


class Solution:
    depth = 0
    def isEq(self, a, b):
        plainA = a.replace("*", "")
        plainB = b.replace("*", "")
        return plainB == "." or plainA == "." or plainA == plainB
    
    def isMultiple(self, a):
        return a[1] == "*"
    
    def isWild(self, a):
        return a[0] == "."
    
    def print(self, s):
        out = " "
        for i in range(self.depth):
            out += "*"
        #print(out+" "+str(s))
    
    def arrayifyExpression(self, regex):
        out = []
        for i in range(len(regex)):
            result = regex[i]
            if result == "*":
                continue
            if i < len(regex) - 1:
                if regex[i+1] == "*":
                    result += "*"
            out.append(result)

        return out

    def smartMatch(self, s, p):
        """
        :type s: list
        :type p: list
        :rtype: bool
        """
        self.depth += 1
        
        if len(p) >= 2:
            while len(p[0]) > 1 and len(p[1]) > 1 and self.isEq(p[0], p[1]):
                self.print("p[0][0] == p[1][0]")
                if self.isWild(p[0]):
                    #.*c* --> .*
                    return self.smartMatch(s, [".*"]+p[2:])
                return self.smartMatch(s, p[1:])

        self.print(str(s)+" ("+str(p)+")")

        if s == p:
            self.depth -= 1
            self.print("s == p")
            return True
        
        multiple = False
        if p:
            multiple = (len(p[0]) == 2)

        match = False
        if p and s:
            match = self.isEq(s[0], p[0])

        if s and not p or (not multiple and not s):
            self.depth -= 1
            self.print("not s or not p")
            return False

        if multiple and not s and len(p) == 1:
            self.depth -= 1
            self.print(" and not s")
            return True

        if multiple and self.smartMatch(s, p[1:]):
            self.print("multiple try s, p[1:]")
            self.depth -= 1
            return True
        
        if match and self.smartMatch(s[1:], p[1:]):
            self.print("match not mul, trying  s[1:] and p[1:]")
            return True        

        if multiple and match and len(s) > 1:
            if self.smartMatch(s[1:], p):
                self.print("smartMatch(s[1:], p)")
                self.depth -= 1
                return True
        
        self.depth -= 1
        self.print("Fallthrough")        
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        string = [x for x in s]
        expression = self.arrayifyExpression(p)
        return self.smartMatch(string, expression)
        
    # def smartMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """        
    #     self.depth += 1

    #     if len(p) >= 4:
    #         while p[1] == "*" and p[3] == "*" and p[0] == p[2]:
    #             self.print("s[0] == p[2]")
    #             p = p[2:]
    #             if len(p) < 4:
    #                 break
        
    #     if s == p:
    #         self.print("s == p")            
    #         self.depth -= 1
    #         return True
    #     if len(p) < 1:
    #         self.print("len(p) == 0")
    #         self.depth -= 1
    #         return False
    #     elif len(s) == 1 and len(p) == 1:
    #         
    #         self.depth -= 1
    #         return self.isEq(s[0], p[0])
    #     elif (len(s) != 1) and len(p) < 2:
    #         self.print("len(s) != 1 and len(p) < 2")
    #         self.depth -= 1
    #         return False
    #     elif p[1] != "*" and len(s) == 0:
    #         self.print("p[1] != '*' and len(s) == 0")
    #         self.depth -= 1
    #         return False
    #     elif p[1] == "*" and len(s) == 0:
    #         self.print("p[1] == '*' and len(s) == 0")
    #         return self.isMatch(s, p[2:])
    #     elif self.isEq(s[0], p[0]) and p[1] == "*" and len(p) > 2:
    #         self.print("p[1] == '*' and len(p) > 2")
    #         if self.isEq(s[0], p[2]):
    #             self.print("s[0] == p[2]")
    #             if self.isMatch(s, p[2:]):
    #                 self.print("s == p[2:]")
    #                 self.depth -= 1
    #                 return True
    #     if p[1] == "*":
    #         self.print("p[1] == '*'")
    #         self.print("try: --"+p[0:2])
    #         if sel11.2f.isMatch(s, p[2:]):
    #             self.depth -= 1
    #             return True
                
    #         while self.isEq(s[0], p[0]) and len(s) > 1:
    #             self.print("s = s[1:]")
    #             s = s[1:]
    #             if self.isMatch(s, p[2:]):
    #                 self.depth -= 1
    #                 return True

    #         if self.isEq(s[0], p[0]) and p[2:] == "":
    #             self.depth -= 1                
    #             return True

    #         if s[0] == p[0]:
    #             self.print("s[0] == p[0]")
    #             self.depth -= 1
    #             return self.isMatch(s[1:], p[2:])
    #         else:
    #             self.print("s[0] != p[0]")
    #             self.depth -= 1
    #             return self.isMatch(s, p[2:])

    #     if self.isEq(s[0], p[0]): 
    #         self.print("s[0] == p[0]")
    #         self.depth -= 1
    #         return self.isMatch(s[1:], p[1:])
            
    #     self.depth -= 1
    #     self.print("Fallthrough")
    #     return False

s = Solution()

assert s.isMatch("", "c*c*") == True
assert s.isMatch("", "c*") == True
assert s.isMatch("","") == True
assert s.isMatch("aa","a") == False
assert s.isMatch("aa","aa") == True
assert s.isMatch("aaa","aa") == False
assert s.isMatch("aaa","aa") == False
assert s.isMatch("aa", "a*") == True
assert s.isMatch("aa", ".*") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aab", "c*a*b") == True
assert s.isMatch("ab", ".*") == True
assert s.isMatch("aaa", "aaaa") == False
assert s.isMatch("aaa", "ab*a*c*a") == True
assert s.isMatch("aaa", "a*a") == True
assert s.isMatch("bbbba", ".*a*a") == True
assert s.isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s") == True
assert s.isMatch("bb", ".bab") == False
assert s.isMatch("abcd", "d*") == False
assert s.isMatch("a", "ab*") == True
assert s.isMatch("ab", ".*..c*") == True
assert s.isMatch("a", ".*..a*") == False
assert s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False
assert s.isMatch("bbaa", "a...") == False
assert s.isMatch('caabbbb','b*.*a*aa*a*b*') == True
assert s.isMatch("ccbbabcaccacbcacaa",".*c*.*.*.c*a*.c") == False
assert s.isMatch("aaaaaaaaaaaaab", "a*a*b") == True
assert s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b") == True

# #needs to be faster than .577 seconds
assert s.isMatch("bccbbabcaccacbcacaa", ".*b.*c*.*.*.c*a*.c") == False
assert s.isMatch("baaabaacaacaacbca", "b*c*c*.*.*bba*b*") == False

#assert s.isMatch("bccbbabcaccacbcacaa", ".*b.*c*.*.*.c*a*.c") == True
#assert s.isMatch("bccbbabcaccacbcacaa", ".*b.*c*.*.c*a*.c") == True

#assert s.isMatch("aaaaaaabaabcaba", ".*") == True
#assert s.isMatch("aaaaaaabaabcaba", "a.*a*a*") == True

#assert s.isMatch("abcaaaaaaabaabcabac", "ab.a.*a*a*.*b*b*") == True

#assert s.isMatch("abaabcabac", "a*a*.*b*b*") == True
#assert s.isMatch("abcaaaaaaabaabcabac", "ab.a.*a*a*.*b*b*") == True

#====Failures:
#assert s.isMatch("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*") == True
#assert s.isMatch("caabbaccbbacaabbbb", ".*b*.*a*aa*a*") == True

#assert s.isMatch("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*") == True
#assert s.isMatch("bcbbcb", "a*.*b.*b.*a*a*a*a*") == True
#assert s.isMatch("abcaba", "a.*b*a*a*") == True

#assert s.isMatch("babaaa", "b.*aa*") == True

#assert s.isMatch("bacaabbbb", "b*.*a*aa*a*") == True
#assert s.isMatch("bacaa", "b*.*a*a") == True
#assert s.isMatch("caabbaccbbacaabbbb", ".*b*.*a*aa*a*") == True
#assert s.isMatch("caabbaccbbacaabbbb", ".*b*.*a*aa*a*") == True

#assert s.isMatch("cab", ".*b*.*a*aa*a*") == True



