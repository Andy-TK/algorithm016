# 题目: LeetCode 236 - 二叉树的最近公共祖先
# 地址: https://leetcode-cn.com/lowest-common-ancestor-of-a-binary-tree/
# 进度: 50%, feedback
# 遍数: 1 遍
# 思路: 递归。如果当前（子）树同时包含 p 和 q，则返回值为其最近公共祖先。如果其中只有一个在该子树中，
#      那么返回值为该结点。如果两者都不在该子树中，则返回值为 None。


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right





