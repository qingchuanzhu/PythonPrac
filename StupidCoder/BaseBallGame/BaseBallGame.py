class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        top = 0
        runningSum = 0
        validNumbers = [None] * len(ops)

        for i in range(len(ops)):
            c = ops[i]
            if c == '+':
                summedScore = validNumbers[top-1] + validNumbers[top-2]
                runningSum += summedScore
                validNumbers[top] = summedScore
                top+=1
            elif c == 'D':
                doubledScore = 2 * validNumbers[top-1]
                runningSum += doubledScore
                validNumbers[top] = doubledScore
                top+=1
            elif c == 'C':
                runningSum -= validNumbers[top-1]
                top-=1
            else:
                runningSum += int(c)
                validNumbers[top] = int(c)
                top += 1

        return runningSum


s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
