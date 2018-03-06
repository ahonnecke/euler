class Solution:
    def isPalindrome(self, s, lpoint, rpoint):
        i=1
        print(str(lpoint)+":"+str(rpoint))
        if rpoint > len(s) - 1:
            return 0
        res = 0
        while s[lpoint] == s[rpoint]:
            lpoint -= 1
            rpoint += 1
            res += 1
            if lpoint < 0:
                break
            if rpoint > len(s) - 1:
                break
        print(res)
        return res
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s
        <
        longest = ""
        for i in range(len(s) -1 ):
            epal = self.isPalindrome(s, i, i+1)
            print("epal: "+str(epal))
            if epal >= len(longest):
                longest = s[i-epal+1:i+1+epal]
                print("i: "+str(i)+" e: "+str(epal)+":"+str(i+1+epal)+" "+str(longest))
            
            opal = self.isPalindrome(s, i, i+2)+2
            print("opal: "+str(opal))
            if opal > len(longest):
                longest = s[i-opal+1:i+2+opal]
                print("o: "+str(longest))
                
        return longest
            
            

s = Solution()
# #print(s.longestPalindrome("aaaa"))
# assert s.longestPalindrome("aaaa") == "aaaa"
# assert s.longestPalindrome("bb") == "bb"
# #print(s.longestPalindrome("cbbd"))
# assert s.longestPalindrome("cbbd") == "bb"
# assert s.longestPalindrome("d") == "d"
print(s.longestPalindrome("ccc"))
# assert s.longestPalindrome("ccc") == "ccc"
# assert s.longestPalindrome("") == ""
# assert s.longestPalindrome("babad") == "bab"
# assert s.longestPalindrome("34567iugfdcvbnmbabadertyuiop") == "bab"
# assert s.longestPalindrome("abb") == "bb"
        
