# 学习笔记 Week 03
## 第 7 节课：泛型递归、树的递归

**注意**：树的面试题解法一般都是递归。
* 节点定义
* 重复性（自相似性）

**二叉树前中后序遍历 Python 实现**：

```Python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```

### 递归 (Recursion)

**递归** 本质上也是一种循环，其与一般 for 和 while 循环的区别在于递归是通过 **函数体** 来进行循环的。

可以类比盗梦空间：

* 向下进入到不同梦境中；向上又回到原来一层
* 通过声音同步回到上一层
* 每一层的环境和周围的人都是一份拷贝、 主角等几个人穿越不同层级的梦境（发生和携带变化）

#### 例子：计算 n!

```Python
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n — 1)
```

<img src="http://andy-blog.oss-cn-beijing.aliyuncs.com/blog/2020-09-27-WX20200927-193824%402x.png" width="40%">

#### 泛型递归代码模板

##### Python

```Python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level
    process(level, data...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
```

##### Java

```Java
public void recur(int level, int param) {
    // terminator
    if (level > MAX_LEVEL) {
        process result
        return;
    }

    // process current logic
    process(level, param);

    // drill down
    recur( level: level + 1, newParam);

    // restore current status
}
```

#### 思维要点

1. 不要人肉进行递归（最大误区）
2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3. 数学归纳法思维

#### 实战题目

* 泛型递归
  1. <https://leetcode-cn.com/problems/climbing-stairs/>
  2. <https://leetcode-cn.com/problems/generate-parentheses/>

* 树的递归
  1. <https://leetcode-cn.com/problems/invert-binary-tree/description/>
  2. <https://leetcode-cn.com/problems/validate-binary-search-tree/>
  3. <https://leetcode-cn.com/problems/maximum-depth-of-binarytree/>
  4. <https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/>
  5. <https://leetcode-cn.com/problems/serialize-and-deserializebinary-tree/>

## 第 8 节课：分治、回溯

本质上，分治和回溯都属于递归方法。

**递归状态树**

<img src="http://andy-blog.oss-cn-beijing.aliyuncs.com/blog/2020-09-27-WX20200927-195047%402x.png" width="70%">

### 分治 (Divide & Conquer)

#### 例子：字符串大小写转换

<img src="http://andy-blog.oss-cn-beijing.aliyuncs.com/blog/2020-09-27-WX20200927-195244%402x.png" width="80%">

#### Python 代码模板

```Python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states
```

### 回溯 (Backtracking)

**回溯** 采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算 (相当于对结果解空间进行剪枝)，再通过其它的可能的分步解答再次尝试寻找问题的答案。

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

* 找到一个可能存在的正确的答案；
* 在尝试了所有可能的分步方法后宣告该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

#### 实战题目

1. <https://leetcode-cn.com/problems/majority-element/description/> (简单、但是高频)
2. <https://leetcode-cn.com/problems/letter-combinations-of-aphone-number/>
3. <https://leetcode-cn.com/problems/n-queens/>

