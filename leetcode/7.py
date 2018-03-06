class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        out = ""
        for i in range(len(s)-1, -1, -1):
            out += s[i]

        outint = int(out)
        
        if x < 0:
            outint = outint * -1

        if abs(outint) >= 2**31-1:
            return 0
        
        return outint

s = Solution()
#print(s.reverse(123))
assert s.reverse(123) == 321

# #print(s.reverse(-123))
assert s.reverse(-123) == -321

# print(s.reverse(1534236469))
assert s.reverse(1534236469) == 0
# print(s.reverse(-2147483412))
assert s.reverse(-2147483412) == -2143847412

print(s.reverse(-2147483648))
assert s.reverse(-2147483648) == 0
