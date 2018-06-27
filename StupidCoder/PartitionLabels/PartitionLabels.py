class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        i = 0
        head = tail = 0
        while i < len(S):
            char = S[i]
            if S.rfind(char) > tail:
                tail = S.rfind(char)
            if i == tail:
                result.append(tail - head + 1)
                head = tail + 1
                tail = head
            i += 1

        return result


s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))
