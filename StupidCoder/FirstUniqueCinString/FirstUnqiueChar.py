class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        A = list(range(len(s)))
        D = {}
        for i in range(len(s)):
            s[i:].find(s[i])
            if s[i] in D:
                A[D[s[i]]] = i
                A[i] = A[i] + 1
            else:
                D[s[i]] = i

        result = -1
        for i in range(len(A)):
            if i == A[i]:
                result = i
                break
        return result


s = Solution()
print(s.firstUniqChar('loveleetcode'))
