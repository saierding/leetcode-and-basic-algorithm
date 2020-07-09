# 994. Rotting Oranges


class Solution:

    # 这个问题类似于岛屿问题，我们只需将所有的烂橘子的坐标
    # 存放到一个队列里面，然后通过BFS将附近的新鲜橘子腐蚀即可。
    def orangesRotting(self, grid) -> int:
        r, c = len(grid), len(grid[0])
        d = [0, 1, 0, -1, 0]
        q = []
        step = cnt = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2: q.append([i, j])
                if grid[i][j] == 1: cnt += 1

        while q:
            if cnt == 0: return step

            n = len(q)
            for _ in range(n):
                x, y = q.pop(0)
                for i in range(4):
                    nx, ny = x + d[i], y + d[i + 1]
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        cnt -= 1
                        q.append([nx, ny])
                        grid[nx][ny] = 2
            step += 1

        return step if cnt == 0 else -1
