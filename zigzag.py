class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        seg = 2 * numRows - 2;
        inc = seg
        for row in range(numRows):
            i = row
            while i < len(s):
                print s[i],
                if inc < seg and inc > 0 and i + inc < len(s):
                    print s[i + inc],
                i += seg
            inc -= 2

test = Solution()
test.convert("PAYPALISHIRING", 4)
