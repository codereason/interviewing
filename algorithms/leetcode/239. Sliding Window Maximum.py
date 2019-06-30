
'''
Solution Using Dequeue: O(N)

Very similar code structure to heap solution
http://yuanhsh.iteye.com/blog/2190852
https://docs.python.org/2/library/collections.html#collections.deque
Add to dequeue at tail using the rule where you pop all numbers from tail which are less than equal to the number. Think why? 300->50->27 and say 100 comes. 50 and/or 27 can never be the maximum in any range.
When you do the above, the largest number is at head. But you still need to test if front is within the range or not.
Pop or push each element at-max once. O(N)
*So, to maintain the queue in order,

When moves to a new number, iterate through back of the queue, removes all numbers that are not greater than the new one, and then insert the new one to the back.
findMax only need to take the first one of the queue.
To remove a number outside the window, only compare whether the current index is greater than the front of queue. If so, remove it.*

使用双端队列，队列元素降序排序，队首元素为所求最大值。滑动窗口右移，若出现的元素比队首（最大元素）大，此时清空队列，并将最大值插入队列。若比当前值小，则插入尾部。每次窗口右移的时候需要判断当前的最大值是否在有效范围，若不在，则需要将其从队列中删除。


遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标

由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)

记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]

若deque中的元素下标＜ i - (k - 1)，则将其从队头弹出，deque中的元素按照下标递增顺序从队尾入队。

这样就确保deque中的数组下标范围为[i - (k - 1), i]，满足滑动窗口的要求。

当下标i从队尾入队时，顺次弹出队列尾部不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）

deque的队头元素即为当前滑动窗口的最大值


利用一个双端队列, 我们可以在O(1)的时间内删除队首和队尾元素, 并且可以在O(1)的时间内随机存取, 也就是说双端队列综合了链表和数组的优点.

在队列中我们存储元素在数组中的位置, 并且维持队列的严格递减, 也就说队首元素最大的,代表在数组中到队首元素那个位置之前最大的数. 

当遍历到一个新元素时, 如果队列里有比当前元素小的, 就将其移除队列, 以保证队列的递减. 

当队列元素位置之差大于k, 就将队首元素移除.
--------------------- 
作者：小榕流光 
来源：CSDN 
原文：https://blog.csdn.net/qq508618087/article/details/51003381 
版权声明：本文为博主原创文章，转载请附上博文链接！

'''
from collections import deque
class Solution(object):
    def add_to_dq(self, dq, nums, i):
        while len(dq) and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        return

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        dq = deque()
        for i in range(k):
            self.add_to_dq(dq, nums, i)
        result, start, end = [], 0, k-1
        while end < len(nums):
            while True:
                if dq[0] >= start:
                    result.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start, end = start+1,end+1
            if end < len(nums):
                self.add_to_dq(dq, nums, end)
        return result
class Solution2:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        '''
        暴力解法
        '''
        if not arr:
            return []
        res = []
        for i in range(len(arr)-k+1):
            res.append(max(arr[i:i+k]))
        return res
        
if __name__ == "__main__":
    nums, k = [1,3,-1,-3,5,3,6,7], 3
    print(Solution().maxSlidingWindow(nums,k))
    