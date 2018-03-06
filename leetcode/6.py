class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = len(s)
        if len(s) <= numRows or i < 2 or numRows == 1:
            return s
        irange = range(int(i-1/numRows)+1)
        output=[["" for j in range(numRows)] for k in irange]
        upAndDownCount = numRows+(numRows-2)
        for i in range(len(s)):
            mod = i % upAndDownCount
            x = int(i / upAndDownCount) * (numRows - 1)
            
            if mod < numRows:
                y = mod
            else:
                x += mod - numRows + 1
                y = numRows - 2 - mod
            
            output[x][y] = s[i]
            
        outstring = ""
        
        for j in range(numRows):
            for i in output:
                outstring += i[j]

        return outstring
    

s = Solution()
# assert s.convert("ABCDEF", 5) == "ABCDFE"
# assert s.convert("ABCDEF", 4) == "ABFCED"
# assert s.convert("ABCDE", 4) == "ABCED"
# assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# #print(s.convert("ABCDEFGHIJKLMNOPXRSTUVWXY", 4))
# assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# assert s.convert("AB", 2) == "AB"
# assert s.convert("AB", 1) == "AB"
# assert s.convert("ABC", 1) == "ABC"
assert s.convert("heltfchqssrwqgwanggkjlsownsdpoowubszfzratjwlpuldarnmehcbvuemiulcxdedcxfygbjyyxbyqqmvxoyukchszuxwxdbbagzjklhiikiyavvzltwwyfqxzpvwszxvfzerknbuxkszhoaujwqhbjecycyrbyoizucjhddgpxfynftxelehulktnkkqkaajucsdgxjvvoukvphzamjvxtomfacqaezwhuzntkkqagbvxkxywgtvbjjijnylsajzwioruaiujlrgvoguwzrzkbivogggiphgzvytygnhtfnovwkuvctidbdrkkaubhbddzwbhmkatzqqvbktdgbgjezvqzqshtxmutpbhzdcyvvwwhpbnqjxujunkmhtfehzzwchxhlydiubqjddbmcxxzkilrdrvlsvjvehcrfhabjqkmvnaykyxviimnbkyufirlpvcwdcxmsjaowaogandkxsybcwvjgouxjytobscvdclbfzkfonqmfqpjmksvaoslnoaqgelmhxnmyxtnllbsbqcocwjendparrsywdkfazrbxmoiyrczjgplfypseguvymvuphzshsteejoccsclzrwesnyytsttgppvwqpfikjpvztxsxirrgxlvvjpnckttaqqqivbshsogllylwrccopylypaabvwbomuwjxqspezcszpqtrsjgsvgjxhltdohrifchvvyawbuxqkskecszzzkyixrnmagwfiebfcdbfxbyjtipxcoybzxjyowkrcjwnpxstawbzxzisjysloqnpnyoevavzjrmarhutdvtcwdwfdoqsffhuexazyvajpnkiugbzdwdzazedowxvchrgeshephogwaosiqtlmwmowssmopjswayduhhkrxqnzhijxbulyiawauirjtjitk", 742) == "heltfchqssrwqgwanggkjlsownsdpoowubszfzratjwlpuldarnmehcbvuemiulcxdedcxfygbjyyxbyqqmvxoyukchszuxwxdbbagzjklhiikiyavvzltwwyfqxzpvwszxvfzerknbuxkszhoaujwqhbjecycyrbyoizucjhddgpxfynftxelehulktnkkqkaajucsdgxjvvoukvphzamjvxtomfacqaezwhuzntkkqagbvxkxywgtvbjjijnylsajzwioruaiujlrgvoguwzrzkbivogggiphgzvytygnhtfnovwkuvctidbdrkkaubhbddzwbhmkatzqqvbktdgbgjezvqzqshtxmutpbhzdcyvvwwhpbnqjxujunkmhtfehzzwchxhlydiubqjddbmcxxzkilrdrvlsvjvehcrfhabjqkmvnaykyxviimnbkyufirlpvcwdcxmsjaowaogandkxsybcwvjgouxjytobscvdclbfzkfonqmfqpjmksvaoslnoaqgelmhxnmyxtnllbsbqcocwjendparrsywdkfazrkbtximjotijyrricuzajwgapilyflyupbsxejgiuhvzynmqvxurpkhhzhsuhdsytaewesjjopcocmsscslwzormwwemslntyqyitssotatwggpophvpweqhpsfeigkrjhpcvvzxtwxosdxeizrarzgdxwldvzvbjgpunickkntptjaaqvqyqziavxbesuhhsfofgslqloydlfwwrdcwccotpvydltyupharaabmvrwjbzovmauvwejoxyqnsppneqzoclsszypjqstirzsxjzgbswvagtjsxxhplntwdjochrrkiwfocyhjvxvzybaywobcuxxpqiktsjkyebcxsfzbzdzckfybiexirfnwmga"
#print(s.convert("ABCD", 3))
# assert s.convert("ABCD", 2) == "ADBC"

