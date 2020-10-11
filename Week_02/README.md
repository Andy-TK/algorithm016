# 学习笔记 Week 02
## 第 5 节课：哈希表、映射、集合

**定义**：**哈希表 (Hash table)**，也叫散列表，是根据 **关键码值 (Key value)** 直接进行访问的数据结构。它通过把关键码值 **映射** 到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫作 **散列函数 (Hash Function)**，存放记录的数组叫作哈希表 (或散列表)。

**工程实践**：
* 电话号码簿
* 用户信息表
* 缓存（LRU Cache）
* 键值对存储（Redis）

**Python 实现**：

```Python
list_x = [1, 2, 3, 4]

map_x = { ‘jack’: 100,
          ‘张三’: 80,
          ‘selina’: 90,
          ...
}

set_x = {‘jack’, ‘selina’, ‘Andy’}
set_y = set([‘jack’, ‘selina’, ‘jack’])
```

**复杂度分析**：

平均情况下，插入、删除、搜索的时间复杂度都是 O(1)；最差情况下 (所有元素都出现哈希碰撞)，采用开链冲突处理策略的哈希表会退化为单向链表，其插入、删除、搜索的时间复杂度将退化为 O(n)。

## 第 6 节课：树、二叉树、二叉搜索树

**注意**：

* Linked List 是特殊化的 Tree (分支因子为 1)
* Tree 是特殊化的 Graph (无环)

### 二叉树的定义

**示例代码：结点类定义**

**Python 实现**：

```Python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```

**Java 实现**：

```Java
public class TreeNode {
    public int val;
    public TreeNode left, right;
    public TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
```

**C++ 实现**：

```C++
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
}
```

### 二叉树的遍历

**3 种遍历类型**：

* 前序（Pre-order）：根-左-右
* 中序（In-order）：左-根-右
* 后序（Post-order）：左-右-根

**前、中、后序遍历图解**：

<img src="http://andy-blog.oss-cn-beijing.aliyuncs.com/blog/2020-09-20-WX20200920-222351%402x.png" width="60%">

**Python 实现**：

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

### 二叉搜索树

二叉搜索树，也称二叉排序树、有序二叉树 (Ordered Binary Tree)、排序二叉树 (Sorted Binary Tree)，是指一棵空树或者具有下列性质的二叉树：

1. 左子树上所有结点的值均小于它的根结点的值；

2. 右子树上所有结点的值均大于它的根结点的值；

3. 以此类推：左、右子树也分别为二叉搜索树。(重复性)

中序遍历：升序排列

**二叉搜索树常见操作**：

1. 查询
2. 插入新结点（创建）
3. 删除

Demo: <https://visualgo.net/zh/bst>

**复杂度分析**：

平均情况下，对于一个相对平衡的二叉搜索树，其查询、插入、删除的时间复杂度均为 O(logn)；最差情况下 (极端不平衡，退化为单链表)，其查询、插入、删除的时间复杂度会退化为 O(n)。

## 第 6 节课：堆和二叉堆

### 堆 (Heap)

**定义**：Heap 是指可以从一堆数据中迅速找到其中最大或最小值的数据结构。(注意：是最大或最小，无法同时满足)

通常，将根结点最大的堆称为大顶堆或者大根堆；将根结点最小的堆称为小顶堆或者小根堆。

**注意**：Heap 只是一种抽象数据接口，其实现可以有多种方式，不同实现方式的复杂度也不同，常见的堆有二叉堆 (复杂度较差，但实现简单)、斐波那契堆、严格斐波那契堆 (复杂度性能最优，工程上最常用) 等。

**常见操作**

假设是大顶堆，其常见操作 (API) 有：

* find-max: O(1)
* delete-max: O(logN)
* insert(create): O(logN) 或者 O(1) (严格斐波那契堆)

(未完待续)





