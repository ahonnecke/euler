# https://leetcode.com/problems/roman-to-integer/description/

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    numerals = [
        {"dec": 1000, "rom": "M"},
        {"dec": 500, "rom": "D"},
        {"dec": 100, "rom": "C"},
        {"dec": 50, "rom": "L"},
        {"dec": 10, "rom": "X"},
        {"dec": 5, "rom": "V"},
        {"dec": 1, "rom": "I"}
    ]
    
    r2i = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
        }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = False
        num = 0
        for r in s[::-1]:
            i = self.r2i[r]
            if last and i < last:
                num -= i
            else:
                num += i
            last = i
        return num
            
            
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        out = ""

        for i in range(len(self.numerals)):
            dec = self.numerals[i]["dec"]
            div = int(num / dec)
            out += div * self.numerals[i]["rom"]
            num -= div * dec
            
        return out.replace("VIIII", "IX").replace("IIII", "IV").replace("XXXX", "XL").replace("LXL", "XC").replace("CCCC", "CD").replace("DCD", "CM")

s = Solution()
# for i in range(1,225):
#     assert s.intToRoman(i) == s.romanToInt(i)
#s.romanToInt("CCCXC")
#print(s.romanToInt("XCVI"))
#assert s.romanToInt("XCVI") == 96
#print(s.romanToInt("MCMXCVI"))
assert s.romanToInt("MCMXCVI") == 1996
#    print(str(i)+": "+s.intToRoman(i))
#print(str(9)+": "+s.intToRoman(9))

# for i in range(1,25):
# print(str(3000)+": "+s.intToRoman(3000))
# print(str(3000)+": "+s.intToRoman(3000))
    
#assert s.intToRoman(400) == "CD"
#assert s.intToRoman(90) == "XC"
# assert s.intToRoman(5) == "V"
# assert s.intToRoman(6) == "VI"
# assert s.intToRoman(1523) == "MDXXIII"
