'''
284. 窥探迭代器
请你在设计一个迭代器，在集成现有迭代器拥有的 hasNext 和 next 操作的基础上，还额外支持 peek 操作。

实现 PeekingIterator 类：

PeekingIterator(Iterator<int> nums) 使用指定整数迭代器 nums 初始化迭代器。
int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
int peek() 返回数组中的下一个元素，但 不 移动指针。
注意：每种语言可能有不同的构造函数和迭代器，但均支持 int next() 和 boolean hasNext() 函数。

 

示例：

输入：
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
输出：
[null, 1, 2, 2, 3, false]

解释：
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,2,3]
peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,2,3]
peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,3]
peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
peekingIterator.hasNext(); // 返回 False
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
对 next 和 peek 的调用均有效
next、hasNext 和 peek 最多调用  1000 次
 

进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

通过次数26,093提交次数33,891
'''


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        
        """
        return self.cache
        

    def next(self):
        """
        :rtype: int
        """
        tmp = self.cache
        self.cache = self.iterator.next()
        # print(self.cache)
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.cache!=-100000 else False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
        
        

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# nums =[1, 2, 3]
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].