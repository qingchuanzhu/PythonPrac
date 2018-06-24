class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A) != len(B):
            return False

        haveSame = False
        numOfDiff = 0

        firstDiff = [None] * 2
        potentialBuddy = False
        D = {}

        for i in range(len(A)):
            if A[i] != B[i] and numOfDiff == 0:
                firstDiff = A[i], B[i]
                numOfDiff += 1
            elif A[i] != B[i] and numOfDiff == 1:
                numOfDiff += 1
                if B[i] == firstDiff[0] and A[i] == firstDiff[1]:
                    potentialBuddy = True
                else:
                    return False
            elif A[i] != B[i] and numOfDiff == 2:
                return False
            elif A[i] in D:
                haveSame = True
            else:
                D[A[i]] = i

        if numOfDiff == 0 and haveSame:
            return True
        elif numOfDiff == 1:
            return False

        return potentialBuddy


s = Solution()
print(s.buddyStrings('aa', 'ba'))
