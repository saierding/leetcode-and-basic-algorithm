# 1254. Number of Closed Islands


class Solution:

    # 使用深度优先遍历，对逐个连通的小岛进行遍历，每次遍历后将小岛的值更改为-1，为防止重复遍历。
    # 分别从四个角开始，对整个珊格的小岛进行遍历。
    # 然后统计走不到的小岛的个数（即0的个数），这些小岛就属于被孤立的小岛。
    def closedIsland(self, grid) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j, val):
            if (0 <= i < m and 0 <= j < n and grid[i][j] == 0):
                grid[i][j] = val
                dfs(i + 1, j, -1)
                dfs(i - 1, j, -1)
                dfs(i, j + 1, -1)
                dfs(i, j - 1, -1)

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j, -1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, -1)
                    res += 1

        return res
