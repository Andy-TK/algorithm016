# 题目: LeetCode 22 - 括号生成
# 地址: https://leetcode-cn.com/problems/generate-parentheses/
# 进度: 50%, feedback
# 遍数: 1 遍
# 思路: 按位逐次递归生成合法括号组合。


from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def _generate(self, left, right, n, s):
        # step1: terminate
        if left == n and right == n:
            # filter the invalid s: 左括号随时可以加，只要不超过 n；右括号需要满足个数上 left > right
            self.result.append(s)
            return None

        # step2: process current logic: left, right
        # step3: drill down
        if left < n:
            self._generate(left + 1, right, n, s + '(')
        if left > right:
            self._generate(left, right + 1, n, s + ')')
        # step4: reverse states

    def generateParenthesis(self, n: int) -> List[str]:
        self._generate(0, 0, n, "")
        return self.result


sol = Solution()
print(sol.generateParenthesis(n=3))


