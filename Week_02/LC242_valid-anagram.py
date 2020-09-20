# 题目: LeetCode 242 - 有效的字母异位词
# 地址: https://leetcode-cn.com/problems/valid-anagram/
# 进度: 50%, feedback
# 遍数: 1 遍
# 解题步骤:
# 1.Clarification: 和面试官确认什么是异位词、是否大小写敏感等。
# 2. Possible Solutions --> optimal (time & space)
#    2.1 暴力法: 先 sort，然后比较 sorted_str 是否相等。时间复杂度 O(NlogN)
#    2.2 哈希表: 统计每个字符的频次 (例如，可以使用 ASCII 码 0-255 作为哈希函数，即哈希表大小为 256)
# 3. Code
# 4. Test cases


class Solution:
    # 1. 暴力法：直接排序后比较
    # 时间复杂度：O(NlogN)
    # 空间复杂度：O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


from collections import Counter
class Solution:
    # 2. 哈希表法：使用内置函数 Counter 构造字典统计字母频数进行比较
    # 时间复杂度：O(N)
    # 空间复杂度：O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
