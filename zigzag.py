class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) <= numRows:
            return s

        result = ""
        seg = 2 * numRows - 2;
        inc = seg
        for row in range(numRows):
            i = row
            while i < len(s):
                result += s[i]
                if inc < seg and inc > 0 and i + inc < len(s):
                    result += s[i + inc]
                i += seg
            inc -= 2
        return result

test = Solution()
print test.convert("PAYPALISHIRING", 1)
