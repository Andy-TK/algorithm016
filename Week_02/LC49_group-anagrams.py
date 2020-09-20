# 题目: LeetCode 49 - 字母异位词分组
# 地址: https://leetcode-cn.com/problems/group-anagrams/
# 进度: 50%, feedback
# 遍数: 1 遍
# 解题步骤:
# 1.Clarification: 所有输入均为小写字母、不考虑答案输出的顺序。
# 2. Possible Solutions --> optimal (time & space)
#    2.1 排序数组分类: 维护一个映射 {String -> List}，其中每个键 K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 K。
#    2.2 按计数分类: 当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。可以将每个字符串 s 转换为字符数 count，
#                  由26个非负整数组成，表示 a，b，c 的数量等。我们使用这些计数作为哈希映射的基础。和方法 1 相比省掉了一次排序操作。
# 3. Code
# 4. Test cases


class Solution:
    # 1. 排序数组分类
    # 时间复杂度：O(NKlogK)，N 是 strs 的长度，而 KK 是 strs 中字符串的最大长度。当遍历每个字符串时，
    #           外部循环具有的复杂度为 O(N)。然后，在 O(KlogK) 的时间内对每个字符串排序。
    # 空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


from collections import defaultdict
class Solution:
    # 2. 按计数分类
    # 时间复杂度：O(NK)，其中 NN 是 strs 的长度，而 KK 是 strs 中字符串的最大长度。计算每个字符串的字符串
    #           大小是线性的，我们统计每个字符串。
    # 空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


