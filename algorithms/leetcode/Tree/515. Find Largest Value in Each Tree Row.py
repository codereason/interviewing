'''
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
'''


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        max_value = []
        import collections
        Queue = collections.deque()
        Queue.append(root)
        while len(Queue) != 0:
            length = len(Queue)
            tmp = float('-inf')
            for i in range(length):
                r = Queue.popleft()
                if r.val > tmp:
                    tmp = r.val
                if r.left:
                    Queue.append(r.left)
                if r.right:
                    Queue.append(r.right)
            max_value.append(tmp)
        return max_value