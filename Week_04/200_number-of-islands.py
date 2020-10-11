# 题目: LeetCode 200 - 岛屿数量
# 地址: https://leetcode-cn.com/problems/number-of-islands/
# 进度: 50%, feedback
# 遍数: 1 遍


# 方法 1：深度优先搜索
# 思路：我们可以将二维网格看成一个无向图，竖直或水平相邻的 1 之间有边相连。为了求出岛屿的数量，
#      我们可以扫描整个二维网格。如果一个位置为 1，则以其为起始节点开始进行深度优先搜索。在深
#      度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。最终岛屿的数量就是我们进行深度
#      优先搜索的次数。
#
# 时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。
# 空间复杂度：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN。
from typing import List
from collections import deque
import copy


class Solution1():
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands


# 方法 2：广度优先搜索
# 思路：同样地，我们也可以使用广度优先搜索代替深度优先搜索。为了求出岛屿的数量，我们可以扫描整个二维网格。
#      如果一个位置为 1，则将其加入队列，开始进行广度优先搜索。在广度优先搜索的过程中，每个搜索到的 1
#      都会被重新标记为 0。直到队列为空，搜索结束。最终岛屿的数量就是我们进行广度优先搜索的次数。
#
# 时间复杂度：O(MN)，其中 M 和 N 分别为行数和列数。
# 空间复杂度：O(min(M,N))，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min(M,N)。

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbors.append((x, y))
                                grid[x][y] = '0'
        return num_islands


grid1 = [['1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0']]

grid2 = [['1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '1', '0', '0'],
         ['0', '0', '0', '1', '1']]

sol1, sol2 = Solution1(), Solution2()
print(sol1.numIslands(grid=copy.deepcopy(grid1)), sol2.numIslands(grid=copy.deepcopy(grid1)))
print(sol1.numIslands(grid=copy.deepcopy(grid2)), sol2.numIslands(grid=copy.deepcopy(grid2)))



