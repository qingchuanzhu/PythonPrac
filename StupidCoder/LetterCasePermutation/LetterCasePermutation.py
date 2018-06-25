class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        result = list()
        if len(S) < 1 or S.isnumeric():
            return [S]
        self.directedPermutation(0, list(S), result)
        return result


    def directedPermutation(self, i, A, result):
        if i == len(A) - 1:
            if A[i].isalpha():
                result.append(''.join(A))
                if A[i].isupper():
                    A[i] = A[i].lower()
                else:
                    A[i] = A[i].upper()
                result.append(''.join(A))
            else:
                result.append(''.join(A))
            return

        if A[i].isalpha():
            self.directedPermutation(i + 1, A, result)
            if A[i].isupper():
                A[i] = A[i].lower()
            else:
                A[i] = A[i].upper()
            self.directedPermutation(i + 1, A, result)
        else:
            self.directedPermutation(i + 1, A, result)


s = Solution()
print(s.letterCasePermutation('3z4'))
