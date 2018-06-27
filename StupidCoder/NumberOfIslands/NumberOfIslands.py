class Solution:
    island = 0
    W = 0
    H = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.island = 0
        self.H = len(grid)
        if self.H == 0:
            return 0
        self.W = len(grid[0])
        if self.W == 0:
            return 0
        for i in range(self.H):
            for j in range(self.W):
                if grid[i][j] != '0':
                    self.DFS(i, j, grid)
                    self.island += 1

        return self.island

    def DFS(self, i, j, grid):
        grid[i][j] = '0'

        if j - 1 >= 0:
            if grid[i][j - 1] == '1':
                self.DFS(i, j - 1, grid)
        if i + 1 < self.H:
            if grid[i + 1][j] == '1':
                self.DFS(i + 1, j, grid)
        if j + 1 < self.W:
            if grid[i][j + 1] == '1':
                self.DFS(i, j + 1, grid)
        if i - 1 >= 0:
            if grid[i - 1][j] == '1':
                self.DFS(i - 1, j, grid)
        return


s = Solution()
print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
