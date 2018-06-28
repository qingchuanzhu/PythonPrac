class Solution:

    axis_boundary = (None, None)

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        dimension = width
        self.axis_boundary = (None, None)
        for i in range((width + 1) // 2):
            self.rotateCells(i, dimension, matrix)
            dimension -= 2

    def rotateCells(self, i, dimension, matrix):
        j = i
        self.axis_boundary = (i, i + dimension - 1)
        while j < dimension - 1 + i:
            temp = matrix[i][j]
            currentPair = (i, j)
            nextPair = self.nextPair(currentPair, dimension - 1)
            while nextPair != (i, j):
                matrix[currentPair[0]][currentPair[1]] = matrix[nextPair[0]][nextPair[1]]
                currentPair = nextPair
                nextPair = self.nextPair(currentPair, dimension - 1)
            matrix[currentPair[0]][currentPair[1]] = temp
            j += 1


    def nextPair(self, currentPair, dist):
        X = currentPair[0]
        Y = currentPair[1]

        if X == self.axis_boundary[0] and Y != self.axis_boundary[0]:
            if Y - dist == X:
                return X, X
            else:
                return self.axis_boundary[0] + dist - (Y - self.axis_boundary[0]), self.axis_boundary[0]
        if X == self.axis_boundary[1] and Y != self.axis_boundary[1]:
            if dist + Y == X:
                return X, X
            else:
                return self.axis_boundary[1] - (dist - self.axis_boundary[1] + Y), self.axis_boundary[1]
        if Y == self.axis_boundary[0] and X != self.axis_boundary[1]:
            if dist + X == self.axis_boundary[1]:
                return self.axis_boundary[1], self.axis_boundary[0]
            else:
                return self.axis_boundary[1], self.axis_boundary[0] + dist - (self.axis_boundary[1] - X)
        if Y == self.axis_boundary[1] and X != self.axis_boundary[0]:
            if X -dist == self.axis_boundary[0]:
                return self.axis_boundary[0], self.axis_boundary[1]
            else:
                return self.axis_boundary[0], self.axis_boundary[1] - (dist - X + self.axis_boundary[0])


s = Solution()
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(matrix)
s.rotate(matrix)
print(matrix)
