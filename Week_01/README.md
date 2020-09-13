# 学习笔记 Week 01
## 第 3 节课：数组、链表、跳表

### 数组 (Array)

* **优点**：简单，随机访问某个元素的时间复杂度为 $O(1)$。
* **缺点**：插入/删除涉及群移操作，其时间复杂度为 $O(n)$。
* **应用**：适用于数据需要频繁访问，但是更新频率较低的场景。

**Python 实现**：

```Python
a = list[1, 2, 3]
```

### 链表 (Linked List)

* **优点**：插入/删除只需要重新设置目标位置的指针即可，时间复杂度为 $O(1)$。
* **缺点**：访问元素必须从表头 head 开始，时间复杂度为 $O(n)$。
* **应用**：适用于对数据修改和添加/删除操作比较频繁的场景，工程应用如 LRU Cache。

**Python 实现**：

```Python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
```

除了基本的单向链表外，还有双向链表和循环链表。

### 跳表 (Skip List)

* **优点**：跳表在链表的基础上增加了多层索引机制，与平衡树和二分查找相比，其原理简单、容易实现、方便扩展、效率更高，且插入/删除/查找的时间复杂度均为 $O(\log n)$。
* **缺点**：插入和删除的时间复杂度高于普通链表，多层索引占用了部分额外存储空间，但总体空间复杂度仍为 $O(n)$。
* **应用**：只能用于元素有序的情况，工程应用如 Redis。

**Python 实现**：

```Python
from random import randint, seed

class Node:  
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        self.next = [None]*height

class SkipList:

    def __init__(self):
        self.head = Node()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.elem == elem:
                return item
        return None

    def contains(self, elem, update = None):
        return self.find(elem, update) != None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def insert(self, elem):
        _node = Node(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(_node.next))
        while len(self.head.next) < len(_node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if self.find(elem, update) == None:
            for i in range(len(_node.next)):
                _node.next[i] = update[i].next[i]
                update[i].next[i] = _node
            self.len += 1

    def remove(self, elem):

        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1

    def printList(self):
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print(x.next[i].elem),
                x = x.next[i]
            print('')
```

## 第 4 节课：栈、队列、双端队列、优先队列

### 栈 (Stack)

**特点**：

* 先进后出 (FILO)
* 添加、删除某个元素的时间复杂度均为 $O(1)$
* 查询某个元素的时间复杂度为 $O(n)$

**操作**：

* `empty()`：判断栈是否为空，$O(1)$
* `size()`：返回栈的大小，$O(1)$
* `top()`：返回栈顶元素 (不出栈)，$O(1)$
* `push(g)`：将元素 `g` 入栈，$O(1)$
* `pop()`：出栈，$O(1)$

**Python 实现**：

可以采用 `list`、`collections.deque`、`queue.LifoQueue` 等方式实现，这里以 `list` 实现为例：

```Python
class Stack:
    def __init__(self, items=[]):
        self.stack = items

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()
```

### 队列 (Queue)

**特点**：

* 先进先出 (FIFO)
* 添加、删除某个元素的时间复杂度均为 $O(1)$
* 查询某个元素的时间复杂度为 $O(n)$

**操作**：

* `empty()`：判断栈是否为空，$O(1)$
* `size()`：返回栈的大小，$O(1)$
* `enqueue()`：入队，在队列后添加元素，$O(1)$
* `dequeue()`：出队，$O(1)$
* `front()`：获取队列第一个元素，$O(1)$
* `rear()`：获取队列最后一个元素，$O(1)$

**Python 实现**：

可以采用 `list`、`collections.deque`、`queue.LifoQueue` 等方式实现，这里以 `list` 实现为例：

```Python
class Queue:
    def __init__(self, items=[]):
        self.queue = items

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0) # 注意: 这里 list 实现涉及群移操作，时间复杂度为 O(n)。

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]
```

### 双端队列 (Double-End Queue, Deque)

实践中，栈和队列应用相对较少，更常用的是双端队列。

**特点**：

* 栈和队列的结合体，两端都可以进行 pop 和 push 操作
* 插入和删除操作的时间复杂度均为 $O(1)$
* 查询的时间复杂度还是 $O(n)$

**Python 实现**：

```Python
from collections import deque

dq = deque([1,2,3])
dq.append(4) # 在右侧添加元素
dq.appendleft(5) # 在左侧添加元素
dq.pop() # 从右侧弹出元素
dq.popleft() # 从左侧弹出元素
```

### 优先队列 (Priority Queue)

**特点**：

* 插入操作的时间复杂度为 $O(1)$
* 取出操作需要按照元素优先级顺序执行，其时间复杂度为 $O(\log n)$
* 底层具体实现的数据结构较为多样和复杂：heap、bst、treap 等

**Python 实现**：

基于 `heapq` 实现：

```Python
import heapq

q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# 结果：
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')
```

基于 `queue.PriorityQueue` 实现：

```Python
from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, 'code'))
pq.put((1, 'eat'))
pq.put((3, 'sleep'))

while not pq.empty():
    next_item = pq.get()
    print(next_item)

# 结果：
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')
```

**注意**：

* Python 提供了几种优先队列实现可以使用。
* `queue.PriorityQueue` 是其中的首选，其具有良好的面向对象的接口。
* `queue.PriorityQueue` 在内部使用了 `heapq`，时间和空间复杂度与 `heapq` 相同，区别在于`PriorityQueue` 是同步的，提供了锁语义来支持多个并发的生产者和消费者。在不同情况下，锁语义可能会带来帮助，也可能会导致不必要的开销。
* 如果某些情况下想避免 `queue.PriorityQueue` 的锁开销，则可以使用 `heapq` 模块。
