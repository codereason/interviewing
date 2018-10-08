'''
布隆过滤器 BITMAP
布隆过滤器是一种概率空间高效的数据结构。它与hashmap非常相似，用于检索一个元素是否在一个集
合中。它在检索元素是否存在时，能很好地取舍空间使用率与误报比例。正是由于这个特性，它被称作
概率性数据结构（probabilistic data structure）。

空间效率
我们来仔细地看看它的空间效率。如果你想在集合中存储一系列的元素，有很多种不同的做法。你可以
把数据存储在hashmap，随后在hashmap中检索元素是否存在，hashmap的插入和查询的效率都非常高。
但是，由于hashmap直接存储内容，所以空间利用率并不高。

如果希望提高空间利用率，我们可以在元素插入集合之前做一次哈希变换。还有其它方法呢？我们可以用
位数组来存储元素的哈希值。还有吗，还有吗？我们也允许在位数组中存在哈希冲突。这正是布隆过滤器
的工作原理，它们就是基于允许哈希冲突的位数组，可能会造成一些误报。在布隆过滤器的设计阶段就允
许哈希冲突的存在，否则空间使用就不够紧凑了。

当使用列表或者集合时，空间效率都是重要且显著的，那么布隆过滤器就应当被考虑。

布隆过滤器基础
布隆过滤器是N位的位数组，其中N是位数组的大小。它还有另一个参数k，表示使用哈希函数的个数。
这些哈希函数用来设置位数组的值。当往过滤器中插入元素x时，h1(x), h2(x), ..., hk(x)所对应
索引位置的值被置“1”，索引值由各个哈希函数计算得到。注意，如果我们增加哈希函数的数量，误报的
概率会趋近于0.但是，插入和查找的时间开销更大，布隆过滤器的容量也会减小。

为了用布隆过滤器检验元素是否存在，我们需要校验是否所有的位置都被置“1”，与我们插入元素的过程
非常相似。如果所有位置都被置“1”，那也就意味着该元素很有可能存在于布隆过滤器中。若有位置未被置
“1”，那该元素一定不存在。

查询某个元素是否在一个集合中。
'''
# !/usr/bin/python
# -*- coding: utf-8 -*-

import mmh3
from bitarray import bitarray

"""
zhihu_crawler.bloom_filter
Implement a simple bloom filter with murmurhash algorithm.
Bloom filter is used to check wether an element exists in a collection, and it has a good performance in big data situation.
It may has positive rate depend on hash functions and elements count.
~~~~~~~~~~~~~~~~
"""

BIT_SIZE = 5000000


class BloomFilter:
    def __init__(self):
        # Initialize bloom filter, set size and all bits to 0
        bit_array = bitarray(BIT_SIZE)
        bit_array.setall(0)

        self.bit_array = bit_array

    def add(self, url):
        # Add a url, and set points in bitarray to 1 (Points count is equal to hash funcs count.)
        # Here use 7 hash functions.
        point_list = self.get_postions(url)

        for b in point_list:
            self.bit_array[b] = 1

    def contains(self, url):
        # Check if a url is in a collection
        point_list = self.get_postions(url)

        result = True
        for b in point_list:
            result = result and self.bit_array[b]

        return result

    def get_postions(self, url):
        # Get points positions in bit vector.
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE

        return [point1, point2, point3, point4, point5, point6, point7]
