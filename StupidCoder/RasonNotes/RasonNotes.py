class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        D1 = {}
        D2 = {}

        for c in ransomNote:
            if c in D1:
                D1[c] += 1
            else:
                D1[c] = 1

        for c in magazine:
            if c in D2:
                D2[c] += 1
            else:
                D2[c] = 1

        for c in D1:
            if c not in D2:
                return False
            elif D2[c] < D1[c]:
                return False

        return True


s = Solution()
print(s.canConstruct('a', 'b'))
