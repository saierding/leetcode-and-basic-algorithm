# 695. Max Area of Island


class Solution(object):

    # 对原始的地图中所有的点都遍历一遍，找出每个点所从属的小岛的最大面积。
    # 把已经走过的路给设成０，即不能再走
    # 再用一个全局的变量，记录所有小岛的最大面积。
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        self.island = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    self.res = max(self.res, self.island)
                    self.island = 0
        return self.res

    def dfs(self, grid, i, j):  # ensure grid[i][j] == 1
        M, N = len(grid), len(grid[0])
        grid[i][j] = 0
        self.island += 1
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < M and 0 <= y < N and grid[x][y]:
                self.dfs(grid, x, y)
