import time


class Solution(object):

    keys = 'abcdefghijklmnopqrstuvwxyz'
    values = [pow(2, c) for c in range(1, 27, 1)]
    dictionary = dict(zip(keys, values))

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
        # Strings consists of lowercase English letters only

        start_time = time.time()
        result = []

        if len(s) < len(p):
            return []

        tempHashRslt = 0
        for c in p:
            tempHashRslt += self.dictionary[c]
        key = tempHashRslt
        tempHashRslt = 0
        for c in s[:len(p)]:
            tempHashRslt += self.dictionary[c]
        previousKey = tempHashRslt
        if previousKey == key:
            result.append(0)
        for i in range(1, len(s) - len(p) + 1, 1):
            previousKey = previousKey - self.dictionary[s[i - 1]] + self.dictionary[s[i + len(p) - 1]]
            if previousKey == key:
                result.append(i)

        print("---- %s complete time ----" % str(time.time() - start_time))
        print(result)
        return len(result)


s = Solution()
print(s.findAnagrams('eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmouek', 'yqrbgjdwtcaxzsnifvhmou'))

