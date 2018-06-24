class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'AEIOUaeiou'
        low = 0
        high = len(s) - 1
        s = list(s)
        while low < high:
            if s[low] in vowels and s[high] in vowels:
                # swap
                temp = s[low]
                s[low] = s[high]
                s[high] = temp
                low += 1
                high -= 1
            elif s[low] in vowels:
                high -= 1
            elif s[high] in vowels:
                low += 1
            else:
                high -= 1
                low += 1

        return ''.join(s)


s = Solution()
print(s.reverseVowels('aA'))
