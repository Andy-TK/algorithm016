# 题目: LeetCode 51 - N 皇后
# 地址: https://leetcode-cn.com/problems/n-queens/
# 进度: 50%, feedback
# 遍数: 1 遍
# 思路: 回溯法

from typing import List


# 方法 1: 回溯
class Solution1:
    # 递归入口
    def __init__(self):
        self.result = []  # 存储合法的棋盘解空间，即最终结果
        self.cols = set()  # 记录之前所有皇后在列发现上的攻击范围
        self.diag45 = set()  # 记录之前所有皇后在 45 度斜线方向上的攻击范围
        self.diag135 = set()  # 记录之前所有皇后在 135 度斜线方向上的攻击范围

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # recursion terminator
        if row >= n:
            self.result.append(cur_state)
            return None

        # current level, do it.
        for col in range(n):  # 遍历列
            if col in self.cols or row + col in self.diag45 or row - col in self.diag135:
                # conflict occurs, stop and go next.
                continue

            # update the flags
            self.cols.add(col)
            self.diag45.add(row + col)
            self.diag135.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            # reverse states
            self.cols.remove(col)
            self.diag45.remove(row + col)
            self.diag135.remove(row - col)

    # 输出棋盘
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i: i + n] for i in range(0, len(board), n)]


# 方法 2: 回溯，更具 Python 风格的写法。
class Solution2:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

# 方法 3: 位运算，后面课程介绍。


N = 8
sol1, sol2 = Solution1(), Solution2()
print("*" * 20 + " Solution1 " + "*" * 20)
print(sol1.solveNQueens(n=N))
print("*" * 20 + " Solution2 " + "*" * 20)
print(sol2.solveNQueens(n=N))

