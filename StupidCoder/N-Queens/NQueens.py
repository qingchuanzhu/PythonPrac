class Solution:

    B = list()
    result = list()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        self.B = list()
        self.result = list()

        for i in range(n):
            self.B.append(['.'] * n)

        self.findPosForRow(n, 0)
        return self.result


    def findPosForRow(self, n, row):
        for col in range(n):
            if self.isValidPos(n, row, col):
                (self.B)[row][col] = 'Q'
                if row == n - 1:
                    self.result.append(self.outPutB(n))
                    self.B[row] = ['.'] * n
                else:
                    self.findPosForRow(n, row + 1)

        if row >= 1:
            self.B[row - 1] = ['.'] * n


    def outPutB(self, n):
        result = list()
        for i in range(n):
            result.append(''.join(self.B[i]))
        return result


    def isValidPos(self, n, row, col):
        for i in range(n):
            if self.B[i][col] == 'Q':
                return False
        for x in range(n):
            y = x + (col - row)
            if y in range(n) and self.B[x][y] == 'Q':
                return False

        for x in range(n):
            y = -x + (col + row)
            if y in range(n) and self.B[x][y] == 'Q':
                return False
        return True


    def solveNQueens2(self, n):
        self.B = [None] * n
        self.result = list()
        self.findPosForRow2(n, 0)
        return self.result


    def findPosForRow2(self, n, row):
        for col in range(n):
            if self.isValidPos2(n, row, col):
                self.B[row] = col
                if row == n - 1:
                    temp = list()
                    for i in range(n):
                        temp.append('.' * self.B[i] + 'Q' + '.' * (n - self.B[i] - 1))
                    self.result.append(temp)
                    self.B[row] = None
                else:
                    self.findPosForRow2(n, row + 1)
        if row >= 1:
            self.B[row] = None


    def isValidPos2(self, n, row, col):
        for i in range(row):
            queen = self.B[i]
            if queen == col or col == row + queen - i or col == -row + queen + i:
                return False
        return True


s = Solution()
print(s.solveNQueens(1))
print(s.solveNQueens(2))
print(s.solveNQueens2(4))
