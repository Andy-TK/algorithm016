# LeetCode 42: 接雨水
# 地址: https://leetcode-cn.com/problems/trapping-rain-water/
# 思路: 双指针，分别计算每个柱子的盛水量并求和。
# 时间复杂度: O(n)
# 空间复杂度: O(1)
# 进度: 50%, waiting for feedback
# 遍数: 1


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if len(height) < 3:
            return water
        j, k = 0, len(height) - 1
        L, R = height[j], height[k]
        while j <= k:
            L, R = max(height[j], L), max(height[k], R)
            if L < R:
                water += L - height[j]
                j += 1
            else:
                water += R - height[k]
                k -= 1
        return water
