
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
    