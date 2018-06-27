class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        # special char: !?',;.

        paragraph = paragraph.rstrip()
        paragraph = paragraph.lstrip()
        paragraph = paragraph.replace('!', '')
        paragraph = paragraph.replace('?', '')
        paragraph = paragraph.replace('\'', '')
        paragraph = paragraph.replace(',', '')
        paragraph = paragraph.replace(';', '')
        paragraph = paragraph.replace('.', '')

        paragraph = paragraph.lower()
        wordsList = paragraph.split()
        D = {}
        freqWord = None
        maxFreq = 0
        for w in wordsList:
            if w not in D:
                if w not in banned:
                    D[w] = 1
                    if maxFreq == 0:
                        maxFreq = 1
                        freqWord = w
            else:
                D[w] += 1
                if D[w] > maxFreq:
                    maxFreq = D[w]
                    freqWord = w

        return freqWord


s = Solution()
print(s.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
