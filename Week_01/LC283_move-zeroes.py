# LeetCode 283: 移动零
# 地址: https://leetcode-cn.com/problems/move-zeroes/
# 思路: 利用一维数组坐标变换，双指针 i 和 j，交换 0 和非 0 元素位置。
# 时间复杂度: O(n)
# 空间复杂度: O(1)
# 进度: 50%, waiting for feedback
# 遍数: 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0  # record the index for the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1