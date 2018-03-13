class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        out = ""
        numerals = [
            {"dec": 1000, "rom": "M"},
            {"dec": 500, "rom": "D"},
            {"dec": 100, "rom": "C"},
            {"dec": 50, "rom": "L"},
            {"dec": 10, "rom": "X"},
            {"dec": 5, "rom": "V"},
            {"dec": 1, "rom": "I"}
            ]

        #this is the consistant algorithmic solution
        for i in range(len(numerals)):
            dec = numerals[i]["dec"]
            rom = numerals[i]["rom"]
            div = int(num / dec)
            out += div * rom
            num -= div * dec
        return out.replace("VIIII", "IX").replace("IIII", "IV").replace("XXXX", "XL").replace("LXL", "XC").replace("CCCC", "CD").replace("DCD", "CM")

s = Solution()
for i in range(1,225):
    print(str(i)+": "+s.intToRoman(i))
#print(str(9)+": "+s.intToRoman(9))

# for i in range(1,25):
# print(str(3000)+": "+s.intToRoman(3000))
# print(str(3000)+": "+s.intToRoman(3000))
    
assert s.intToRoman(400) == "CD"
assert s.intToRoman(90) == "XC"
# assert s.intToRoman(5) == "V"
# assert s.intToRoman(6) == "VI"
# assert s.intToRoman(1523) == "MDXXIII"
