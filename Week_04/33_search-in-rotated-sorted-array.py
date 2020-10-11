# 题目: LeetCode 33 - 搜索旋转排序数组
# 地址: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# 进度: 50%, feedback
# 遍数: 1 遍
# 思路: 二分查找
# 要求时间复杂度 O(logN)，可以使用二分查找。
# 注意: 数组本身不是有序的，进行旋转后只保证了数组的局部是有序的。
# 当我们将数组从中间分开成左右两部分时，一定有一部分的数组是有序的。因此，我们可以在常规二分查找时查看当前以 mid 为中心
# 分割出的两部分 [l, mid] 和 [mid + 1, r] 中哪一个是有序的，并根据有序的那个部分确定我们该如何改变二分查找的上下界，
# 因为我们能够根据有序的那部分判断出 target 是否在这个部分：
# (1) 如果 nums[mid] == target, 则返回 mid。
# (2) 如果 [l, mid - 1] 是有序数组，且 target 的大小在区间 [nums[l],nums[mid]] 内，
#     则将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
# (3) 如果 [mid, r] 是有序数组，且 target 的大小在区间 [nums[mid+1],nums[r]] 内，
#     则将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


sol = Solution()
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
