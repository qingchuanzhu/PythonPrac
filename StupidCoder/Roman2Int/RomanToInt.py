class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key = 'IVXLCDM'
        value = [1, 5, 10, 50, 100, 500, 1000]
        D = dict(zip(key, value))

        result = 0

        for c in s:
            result += D[c]
        result -= s.count('IV') * 2
        result -= s.count('IX') * 2
        result -= s.count('XL') * 20
        result -= s.count('XC') * 20
        result -= s.count('CD') * 200
        result -= s.count('CM') * 200

        return result

s = Solution()
print(s.romanToInt('XCD'))
