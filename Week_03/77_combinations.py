# 题目: LeetCode 77 - 组合
# 地址: https://leetcode-cn.com/combinations/
# 进度: 50%, feedback
# 遍数: 1 遍

from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = list(combinations(range(1, n+1), k))
        return [list(comb) for comb in combs]


sol = Solution()
print(sol.combine(n=4, k=2))
