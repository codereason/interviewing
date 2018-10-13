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
        max_value.append(root.val)
        while len(Queue) != 0:

            length = len(Queue)

            for i in range(length):
                r = Queue.popleft()

                if r.left:
                    Queue.append(r.left)
                if r.right:
                    Queue.append(r.right)
            tmp = []
            for i in Queue:
                tmp.append(i.val)
            print(tmp)
            if len(tmp) > 0:
                max_value.append(max(tmp))

        return max_value