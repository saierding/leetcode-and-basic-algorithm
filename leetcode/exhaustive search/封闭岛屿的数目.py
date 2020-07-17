# 1254. Number of Closed Islands


class Solution:
    # 1.我们对每个grid[i][j]为0的点执行深度优先搜索。
    # 2.有一个类变量isopened来记录深度优先搜索的结果，
    # isopened默认为false，如果在深度优先搜索中某个点超出了边界
    #（说明某个边界有0，这个连通图不是closed的），执行完深度优先搜索后，
    # 如果isopened为false，将计数器 + 1，封闭连通图数量 + 1。
    # 时间复杂度O(mn)，

    isopened = False

    def closedIsland(self, grid) -> int:
        n, m, res = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    self.isopened = False
                    self.DFS(grid, i, j, n, m)
                    if not self.isopened: res += 1
        return res

    def DFS(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >= n or y >= m:
            self.isopened = True
            return
        if grid[x][y] == 1:
            return
        grid[x][y] = 1
        self.DFS(grid, x - 1, y, n, m), self.DFS(grid, x + 1, y, n, m), self.DFS(grid, x, y - 1, n, m), self.DFS(grid,
                                                                                                                 x,
                                                                                                                 y + 1,
                                                                                                                 n, m)
